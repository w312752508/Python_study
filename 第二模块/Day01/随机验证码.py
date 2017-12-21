import random
while True:
    check_num = ""
    for i in range(4):
        cun = random.randint(0,4)
        if cun == i :
            tmp = chr(random.randint(65,90))
        else:
            tmp = random.randint(0,9)
        check_num+=str(tmp)
    print("本次验证码：",check_num)
    in_put = input("\033[33;1m请输入验证码：\033[0m")
    if str(in_put.upper()) == check_num :
         print("\033[31;1m恭喜，输入正确，通过验证！\033[0m")
         break
    else:
        print("\033[41;1m输入错误，重新输入验证！\033[0m")

