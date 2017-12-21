import re,json
with open("staff_table", "r") as st:
    staff_list = json.load(st)
Fun_Sel = input("1、查询员工信息\n"
                "2、添加新员工信息\n"
                "3、修改员工信息\n"
                "4、删除员工信息"
                "请选择功能：")

def creat_lsit(user_input):
    """
    :param user_input:获取字符串 user_input
    :return: user_input_list_new, user_input_list, target_list三个列表
    """
    user_input_list_new = user_input.split(" ")
    user_input_list = []
    for i in range(len(user_input_list_new)):
        if user_input_list_new[i] == "":
            continue
        elif "\"" in user_input_list_new[i]:
            user_input_list.append(user_input_list_new[i].replace("\"", ""))
        else:
            user_input_list.append(user_input_list_new[i])
    target_list = user_input_list[1].split(",")
    return user_input_list_new, user_input_list, target_list

if Fun_Sel == "1" :
    while True:
        user_input = input("输入查询命令：")
        user_input_list_new, user_input_list, target_list = creat_lsit(user_input)
        def screen_list_func():
            """
            从字典中获取符合筛选条件的建跟值，以列表的形式返回
            :return: 返回id_dic列表
            """
            b = user_input_list[-2]
            c = user_input_list_new[-1]
            if "=" in b:
                b = '=' + b
            a = user_input_list[-3]
            screen_list = []
            if a == 'staff_id':
                for k, v in staff_list.items():
                    screen_list.append(k, )
            elif a == 'age':
                for k, v in staff_list.items():
                    if eval(v[1] + b + c):
                        screen_list.append([k, v[1]])
            elif a == 'name':
                for k, v in staff_list.items():
                    if eval(v[0].upper() + b + c.upper()):
                        screen_list.append([k, v[0]])
            elif a == 'phone':
                for k, v in staff_list.items():
                    if eval(v[2] + b + c):
                        screen_list.append([k, v[2]])
            elif a == 'dept':
                for k, v in staff_list.items():
                    if eval(("\"" + v[3] + "\"").upper() + b + c.upper()):
                        screen_list.append([k, v[3]])
            elif a == 'enroll_date':
                for k, v in staff_list.items():
                    c = c.replace("\"", "")
                    if c in v[4]:
                        screen_list.append([k, v[4]])
            id_dic = {}
            for n in range(len(screen_list)):
                a = screen_list[n][0]
                id_dic[int(a)] = staff_list[a]
            return id_dic
        def select_func(dic_list):
            """
            以id_dic列表0下标的值做建，从staff_list字典中获取对应的值。
            再根据搜索语句中想要显示的内容筛选显示最终结果
            """
            staff_id_list = []
            name_list = []
            age_list = []
            phone_list = []
            dept_list = []
            enroll_date_list = []
            return_list = []
            all_list = []
            for k, v in dic_list.items():
                staff_id_list.append(k)
                name_list.append(v[0])
                age_list.append(v[1])
                phone_list.append(v[2])
                dept_list.append(v[3])
                enroll_date_list.append(v[4])
                all_list.append(v)
            for target in target_list :
                if target == 'staff_id':
                    return_list.append(staff_id_list)
                elif target == 'name':
                    return_list.append(name_list)
                elif target == 'age':
                    return_list.append(age_list)
                elif target == 'phone':
                    return_list.append(phone_list)
                elif target == 'dept':
                    return_list.append(dept_list)
                elif target == 'enroll':
                    return_list.append(enroll_date_list)

            if "*" in target_list :
                for i in range(len(all_list)):
                    print(all_list[i])
                print("\033[41;1m共找到符合条件的数量：%s\033[0m \n" %(len(all_list)))
            else:
                return_list_new = []
                for l in range(len(return_list[0])):
                    return_list_new.insert(l,[])
                    for s in range(len(return_list)):
                        a = return_list[s][l]
                        return_list_new[l].insert(s, a)
                for i in range(len(return_list_new)):
                    print(return_list_new[i][0],",",return_list_new[i][1])
                print("\033[41;1m共找到符合条件的数量：%s\033[0m \n" % (len(return_list_new)))
        staff_list_new = screen_list_func()
        select_func(staff_list_new)

if Fun_Sel == "2" :
    while True:
        new_staff_inf = input("\033[31;1m输入新员工信息：\033[0m").split(",")
        n_key = len(staff_list)+1
        staff_list["%s" %n_key] = new_staff_inf
        with open("staff_table", "w") as st:
            json.dump(staff_list, st)

if Fun_Sel == "3" :
    user_input = input("输入修改命令：")
    user_input_list_new, user_input_list, target_list = creat_lsit(user_input)
    b = user_input_list[-2]
    c = user_input_list_new[-1]
    d = target_list[-1]
    if "=" in b:
        b = '=' + b
    a = user_input_list[-3]
    screen_list = []
    if a == 'staff_id':
        for k, v in staff_list.items():
            screen_list.append(k, )
    elif a == 'age':
        for k, v in staff_list.items():
            if eval(v[1] + b + c):
                screen_list.append([k, v[1]])
    elif a == 'name':
        for k, v in staff_list.items():
            if eval(("\"" + v[0] + "\"").upper() + b + c.upper()):
                staff_list[k][0] = d
            with open("staff_table", "w") as st:
                json.dump(staff_list, st)
    elif a == 'phone':
        for k, v in staff_list.items():
            if eval(v[2] + b + c):
                screen_list.append([k, v[2]])
    elif a == 'dept':
        i = 0
        for k, v in staff_list.items():
            if eval(("\"" + v[3] + "\"").upper() + b + c.upper()):
                staff_list[k][3] = d
                i+=1
            with open("staff_table", "w") as st:
                json.dump(staff_list, st)
        print("共修改\033[31;1m%s\033[0m记录" %i)
    elif a == 'enroll_date':
        for k, v in staff_list.items():

            c = c.replace("\"", "")
            if c in v[4]:
                screen_list.append([k, v[4]])

if Fun_Sel == "4" :
    del_staff_inf = input("\033[41;1m输入删除员工编号：\033[0m")
    staff_list.pop(del_staff_inf)
    with open("staff_table", "w") as st:
        json.dump(staff_list, st)

