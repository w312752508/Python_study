
'''
猜数字3、7、3的倍数、7的倍数游戏
'''
while True:
    num = input("输入数字：")
    if num == "q" :
        break
    elif int(num)%3==0 or int(num)%7==0 or str("3") in str(num) or str("7") in str(num):
        print(">>>PASS\n")
    else:
        print(">说出数字：",num,"\n")