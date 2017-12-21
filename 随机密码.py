#date:.2017/11/4
import random
while True:
    check_num = ""
    for i in range(8): #获取随机字符
        tmp = chr(random.randint(33, 122))
        check_num +=str(tmp)
    def chr_list(lang,n): #定义需要对比的字符
        a_list = []
        b = n
        for i in range(lang):
            tmp = chr(b)
            a_list.append(str(tmp))
            b += 1
        return a_list

    num_list1 = chr_list(14, 33)
    num_list2 = chr_list(9, 48)
    num_list3 = chr_list(6, 58)
    num_list4 = chr_list(25, 65)
    num_list5 = chr_list(25, 97)

    def jud(num_list,check_num): #判断字符里有没有要判断的字符
        judge_list = []
        for c in check_num:
            if c in num_list:
                judge = True
                judge_list.append(judge)
            else:
                judge = False
                judge_list.append(judge)
        if True in judge_list:
            a = True
        else:
            a = False
        return a

    j1 = jud(num_list1,check_num)
    j2 = jud(num_list2,check_num)
    j3 = jud(num_list3,check_num)
    j4 = jud(num_list4,check_num)
    j5 = jud(num_list5,check_num)

    jud_all = []
    jud_all.append(j1)
    jud_all.append(j2)
    jud_all.append(j3)
    jud_all.append(j4)
    jud_all.append(j5)
    if all(jud_all):
        print(check_num)
        break
    else:
        continue
