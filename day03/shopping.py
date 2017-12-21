import os
name_list = {"zs":"zs","ls":"ls","ww":"ww"} #用户账密
list = [
    ("iphone",6000),
    ("san",3000),
    ("sony",3500),
    ("mi",2000),
]
shop = [] #购物车清单
while True :
    name = input("输入登录名字：")
    passwd = input("输入密码：")
    coun = 0
    if name in name_list.keys() and passwd == name_list[name] :
        print("\033[33;1m欢迎光临!\033[0m\n")
        if os.path.exists("%s.txt" %name) :
            f = open("%s.txt" %(name), "r", encoding="utf-8" )
            print("上次购物明细：\n",f.read(),'\n')
            f.close()
        while True :
            sala = int(input("输入月薪："))
            for i in list :
                print(list.index(i),i)
            while True :
                num_list = input("\n>>>输入想要够买商品的编号：")
                if num_list.isdigit() and int(num_list) < len(list) :
                    sala -= list[int(num_list)][1]
                    if sala >= 0 :
                        shop.append(list[int(num_list)])
                        print(shop,"\n剩余资金:\033[31;1m%s\033[0m\n"  %(sala) )
                        f = open("%s.txt" %(name),"w",encoding="utf-8")
                        f.write(repr(shop))
                        f.write("\n剩余资金:%s" %(sala) )
                        f.close()
                        continue
                    else:
                        print("\033[41;1m余额不足,无法购买，请选择其它商品或退出。\033[0m")
                        sala += int(list[int(num_list)][1])
                        continue
                elif num_list == "q" :
                    print("\n已购买商品:\n%s\n\033[31;1m余额:%s\033[0m\n欢迎下次光临，再见！"%(shop,sala))
                    coun = 1
                    break
                else :
                    print("\033[31;1m输入编号不存在，请重新输入。\033[0m\n")
            if coun == 1 :
                break
    if coun == 1:
        break
    else:
        print("\033[41;1m用户密码错误，请重新输入\033[0m\n")
        continue
