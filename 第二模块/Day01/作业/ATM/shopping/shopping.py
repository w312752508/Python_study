import sys,os,json,logging,time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def shopping(user):
    list = [
        ("iphone",600),
        ("san",300),
        ("sony",350),
        ("mi",200),
    ]
    shop = [] #购物车清单
    while True :
        file_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        with open(r"%s\datebase\user_date" % file_path, "r") as user_date:
            user_info = json.load(user_date)

        #判断打印上次购物记录
        name = user
        if os.path.exists(r"%s\datebase\%s.txt" %(file_path,name)) :
            f = open(r"%s\datebase\%s.txt" %(file_path,name), "r")
            print("上次购物明细：\n",f.read())
            print("银行卡剩余金额：\033[31;1m%s元\033[0m" %(user_info[user]))
            f.close()
        while True :
            sala = user_info[user]
            print("商品清单：")
            for i in list :
                print(list.index(i),i)
            while True :
                num_list = input(">>输入想要够买商品的编号：")
                if num_list.isdigit() and int(num_list) < len(list) :
                    sala -= list[int(num_list)][1]
                    if sala >= 0 :
                        shop.append(list[int(num_list)])
                        print(shop,"\n剩余资金:\033[31;1m%s\033[0m\n"  %(sala) )
                        f = open(r"%s\datebase\%s.txt" %(file_path,name), "w")
                        f.write(repr(shop))
                        f.close()
                        user_info[user] = sala
                        with open(r"%s\datebase\user_date" % file_path, "w") as user_date:
                            json.dump(user_info,user_date)
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