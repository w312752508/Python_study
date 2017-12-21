import re,functools
a = '1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
a = re.sub(" ","",a)
# print(eval(a))

#return chars
def symbol_handler(chars):
    '''处理特殊符号'''
    chars = chars.replace("++", "+")
    chars = chars.replace("+-", "-")
    chars = chars.replace("-+", "-")
    chars = chars.replace("--", "+")
    return chars

#return nu_list[0]
def multiply_handler(chars_list):
    nu_list = re.split("\*",chars_list)
    nu_list_new = []
    for i in nu_list:
         if "/" in i:
             i_list = re.split("/",i)
             for k in range(len(i_list)-1):
                  a = float(i_list[0]) / float(i_list[1])
                  del(i_list[:2])
                  i_list.insert(0,a)
             nu_list_new.append(i_list[0])
         else:
              nu_list_new.append(i)
    nu_list = nu_list_new
    for i in range(len(nu_list)-1):
         a = float(nu_list[0]) * float(nu_list[1])
         del(nu_list[:2])
         nu_list.append(a)
    return nu_list[0]

#return nu_list[0]
def add_subtract_handler(add_char_list):
    """
    :param add_char_list:计算只有+-运算符的字符串 
    :return:打印计算结果 
    """

    """
    处理 - 开头的字符串 
    """
    add_char_list = symbol_handler(add_char_list) #处理特殊符号
    if re.search("^-",add_char_list):
        nu_list = re.split("\+", add_char_list)  # +分割后的列表
        add_char_list = add_char_list.replace(nu_list[0],"")
        add_char_list = add_char_list + nu_list[0]
        add_char_list = symbol_handler(add_char_list)
    if re.search("^\+",add_char_list):
         add_char_list = re.sub("^\+","",add_char_list)

    """
    处理非 - 开头的字符串
    """
    nu_list = re.split("\+", add_char_list)  # +分割后的列表
    nu_list_new = []  # 转储用空列表
    for i in nu_list:  # 循环处理分割后的列表
         if "-" in i:
              i_list = re.split("-", i)  # 将有-号的值再分割成列表
              for k in range(len(i_list) - 1):  # 循环计算列表前两个数相减的值，直到只剩一个数
                   a = float(i_list[0]) - float(i_list[1])
                   del (i_list[:2])
                   i_list.insert(0, a)  # 在列表开头插入新计算出的值继续计算
              nu_list_new.append(i_list[0])  # 将 i处理后的值添加至列表
         else:
              nu_list_new.append(i)  # i不含-号，直接添加至新列表
    nu_list = nu_list_new  # 将nu_list_new的值直接赋值给nu_list
    for i in range(len(nu_list) - 1):
         a = float(nu_list[0]) + float(nu_list[1])
         del (nu_list[:2])
         nu_list.append(a)
    return nu_list[0]

def creat_list(a):
    """
    :param a:去除最底层括号 
    :return: 括号内的值替换原括号的内容
    """
    a = symbol_handler(a)
    b = re.findall(r'\([^()]+\)', a)  # 提取最底层（）列表
    # print(b)
    p_list = []
    for i in b:
        c = re.sub("[\(\)]", "", i)  # 去（）
        # print(c)
        c_list = re.split("[+-]", c)  # 以+-分割c，形成只有*/的列表,计算出结果后替换原对应字符
        if c_list[0] == "": #列表第一个值为空时（既字符串是以-号开头），将第二个值赋值位负数
            new_value = -multiply_handler(c_list[1])
            # print(new_value)
            d = "-"+ c_list[1]
            del(c_list[0:2])
            # c_list.insert(0,new_value)
            c = c.replace(d,str(new_value))
        else:
            for k in c_list:
                if "[*/]" not in k:
                    continue
                else:
                    new_k = multiply_handler(k)
                    c = c.replace(k,str(new_k))
        print(c)
        new_add_value = add_subtract_handler(c)
        a = a.replace(i,new_add_value)
        print(a)
    return a

num_level = re.search("\([^)]+\)", a).group() #获取最多（）的层数
count = num_level.count("(")
# print(count)
for i in range(count):
    a = creat_list(a)
print(a)
