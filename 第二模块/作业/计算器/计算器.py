import re

#特殊字符处理return chars
def symbol_handler(chars):
    '''处理特殊符号'''
    chars = chars.replace("++", "+")
    chars = chars.replace("+-", "-")
    chars = chars.replace("-+", "-")
    chars = chars.replace("--", "+")
    return chars

# 乘除运算return nu_list[0]
def multiply_handler(chars_list):
    chars_list = symbol_handler(chars_list)
    nu_list = re.split("[*/]", chars_list)
    if len(nu_list) == 1:
        nu_list[0] = nu_list[0]
    elif len(nu_list) == 2 and "*" in chars_list:
        nu_list[0] = float(nu_list[0]) * float(nu_list[1])
    elif len(nu_list) == 2 and "/" in chars_list:
        nu_list[0] = float(nu_list[0]) / float(nu_list[1])
    elif len(nu_list) > 2:
        nu_list = re.split("\*", chars_list)
        nu_list_new = []
        for i in nu_list:
            if "/" in i:
                i_list = re.split("/", i)
            for k in range(len(i_list) - 1):
                k_value = float(i_list[0]) / float(i_list[1])
                del (i_list[:2])
                i_list.insert(0, k_value)
                nu_list_new.append(i_list[0])
            else:
                nu_list_new.append(i)
        nu_list = nu_list_new
        for i in range(len(nu_list) - 1):
            k_value = float(nu_list[0]) * float(nu_list[1])
            del (nu_list[:2])
            nu_list.append(k_value)
    return str(nu_list[0])

# 加减运算return nu_list[0]
def add_subtract_handler(add_char_list):
    """
    :param add_char_list:计算只有+-运算符的字符串 
    :return:打印计算结果 
    """
    add_char_list = symbol_handler(add_char_list)  # 处理特殊符号
    nu_list = re.split("[\+-]", add_char_list)
    if len(nu_list) == 1:
        nu_list[0] = nu_list[0]
    elif len(nu_list) == 2:
        if nu_list[0] == "":
            nu_list[0] = "-" + nu_list[1]
        elif nu_list[0] != "" and "-" in add_char_list:
            nu_list[0] = float(nu_list[0]) - float(nu_list[1])
        elif nu_list[0] != "" and "+" in add_char_list:
            nu_list[0] = float(nu_list[0]) + float(nu_list[1])
    elif len(nu_list) > 2:
        nu_list = re.split("\+", add_char_list)  # +分割后的列表
        nu_list_new = []  # 转储用空列表
        for i in nu_list:  # 循环处理分割后的列表
            if "-" in i:
                i_list = re.split("-", i)  # 将有-号的值再分割成列表
                for k in range(len(i_list) - 1):  # 循环计算列表前两个数相减的值，直到只剩一个数
                    if i_list[0] == "":
                        k_new = - float(i_list[1])
                        del (i_list[:2])
                        i_list.insert(0, str(k_new))
                    else:
                        k_new = float(i_list[0]) - float(i_list[1])
                        del (i_list[:2])
                        i_list.insert(0, str(k_new))  # 在列表开头插入新计算出的值继续计算
                nu_list_new.append(i_list[0])  # 将 i处理后的值添加至列表
            else:
                nu_list_new.append(i)  # i不含-号，直接添加至新列表
        nu_list = nu_list_new  # 将nu_list_new的值直接赋值给nu_list
        for i in range(len(nu_list) - 1):
            a = float(nu_list[0]) + float(nu_list[1])
            del (nu_list[:2])
            nu_list.append(a)
    return str(nu_list[0])

# 加减乘除混合运算
def mixture_handler(mixture_char):
    """
    :param mixture_list:混合运算 
    :return: 返回计算结果
    """
    mixture_char = symbol_handler(mixture_char)  # 处理特殊符号
    mixture_char = re.sub("[()]", "", mixture_char)  # 去除（）
    num_len = re.split("[\+-]", mixture_char)
    if len(num_len) == 1 and re.search("[*/]", num_len[0]):  # 只有乘除的正数
        mixture_char = multiply_handler(num_len[0])
    elif len(num_len) == 1 and "*" not in num_len[0] and "/" not in num_len[0]:  # 只有一个正数
        mixture_char = mixture_char
    if len(num_len) == 2:
        if num_len[0] == "" and re.search("[*/]", mixture_char):  # 负数开头的乘除
            mixture_char = "-" + multiply_handler(num_len[1])
        elif num_len[0] == "" and '*' not in mixture_char and "/" not in mixture_char:  # 只有负数
            mixture_char = "-" + num_len[1]
        elif num_len[0] != "" and '*' not in mixture_char and "/" not in mixture_char:  # 只有加减的数
            mixture_char = add_subtract_handler(mixture_char)
        elif num_len[0] != "":
            if num_len[0].endswith("/") or num_len[0].endswith("*"):
                # 有乘除和/- 的数
                mixture_char = multiply_handler(mixture_char)
            elif "-" in mixture_char and re.search("[*/]", mixture_char):
                # 有乘除和-的数
                mixture_char = float(multiply_handler(num_len[0])) - float(multiply_handler(num_len[1]))
            elif "+" in mixture_char and re.search("[*/]", mixture_char):
                # 有乘除和+的数
                mixture_char = float(multiply_handler(num_len[0])) + float(multiply_handler(num_len[1]))
    elif len(num_len) > 2 and re.search("[*/]", mixture_char):
        mixture_list = re.split("[+-]", mixture_char)
        if "*" or "/" in mixture_list:  # 判断列表值含有*/或者/- *-特殊运算符
            for i in mixture_list:
                if i.endswith("/") or i.endswith("*"):  # 先判断/- *-特殊运算符
                    i_next_index = mixture_list.index(i) + 1  # i下一位数的下标
                    i_new = i + "-" + mixture_list[i_next_index]
                    i_new_value = multiply_handler(i_new)
                    mixture_char = mixture_char.replace(i_new, i_new_value)  # 替换/-或者*-特殊组合
                    mixture_char = symbol_handler(mixture_char)
                    continue
                elif "*" in i or "/" in i:
                    i_value = multiply_handler(i)
                    mixture_char = mixture_char.replace(i, i_value)  # 替换/或者*组合
                    mixture_char = symbol_handler(mixture_char)
        else:
            mixture_char = add_subtract_handler(mixture_char)
        mixture_char = add_subtract_handler(mixture_char)
    return str(mixture_char)

#去除（）计算字符串
def calc(a):
    """
    :param a:去除最底层括号 
    :return: 括号内的值替换原括号的内容
    """
    while True:
        if "(" in a :
            b_list = re.findall(r'\([^()]+\)', a)  # 提取最底层（）列表
            for i in b_list:
                i_new = mixture_handler(i)
                a = a.replace(i,i_new)
                a = symbol_handler(a)
        else:
            break
    print("\033[31;1m %s\033[0m " %mixture_handler(a))

# a = '1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
while True:
    a = input("输入需要计算的公式,或输入“b”退出：\n>>")
    a = re.sub(" ","",a)
    if a.upper() == "B" :
        break
    else:
        calc(a)