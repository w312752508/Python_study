import os, os.path, sys, json


def f_to_d_and_del(file_name, input_if):
    dic = {}
    with open(file_name) as f:
        for i in f:
            if i[0] not in [' ', '\t']:
                dic[i] = []
                lst = dic[i]
            else:
                lst.append(i)
    with open("file_name", "w", encoding="utf-8") as f1:
        coun = 0
        for k in dic:
            if input_if in k:
                k_key = k
                coun = 1
        if coun == 1:
            dic.pop(k_key)
        for k1 in dic:
            f1.write(k1)
            for v1 in dic[k1]:
                f1.write(v1)
                f1.flush()


while True:
    choose = input("\n程序功能列表："
                   "\n1、增加配置\n2、删除配置\n3、更改配置\n4、查询配置"
                   "\n\033[33;1m请选择需要的操作的编号：\033[0m")
    if choose == "1":
        new_backend = input("New backend name :")
        server1 = input("server1:")
        server2 = input("server2:")
        weight = input("weight:")
        maxconn = input("maxconn:")
        with open("file", "r", encoding="utf-8") as f, \
                open("file_bak", "w", encoding="utf-8") as f_new:
            for line in f:
                f_new.write(line)
        dic = {}
        with open('file') as f:
            for i in f:
                if i[0] not in [' ', '\t']:
                    dic[i] = []
                    lst = dic[i]
                else:
                    lst.append(i)
        with open("file", "w", encoding="utf-8") as f1:
            coun = 0
            for k in dic:
                if new_backend in k:
                    k_key = k
                    coun = 1
            if coun == 1:
                dic.pop(k_key)
            for k1 in dic:
                f1.write(k1)
                for v1 in dic[k1]:
                    f1.write(v1)
                    f1.flush()
            f1.write("\nbackend %s\n\t\tserber %s %s weight %s maxconn %s" \
                     % (new_backend, server1, server2, weight, maxconn))
            continue
    if int(choose) == "2":
        backend_del = input("\n请输入要删除的backend域名：")
        file_to_dic(file_name="file")
        coun = 0
        for i in dic:
            if backend_del in i:
                k_pop = i
                coun = 1
            if coun == 1:
                dic.pop(k_pop)

    # if int(choose) == "3":
    if choose == "4":
        backend_find = input("\n请输入backend域名：")
        dic = {}
        with open("file", "r", encoding="utf-8") as f4:
            for i in f4:
                if i[0] not in [' ', '\t']:
                    dic[i] = []
                    lst = dic[i]
                else:
                    lst.append(i)
            for i in dic:
                if backend_find in i:
                    for j in dic[i]:
                        print(j, end='')
            continue
    elif choose.lower() == "q":
        break
    else:
        print("\033[41;1m无此功能编号，请重新输入\033[0m")