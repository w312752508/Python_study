import socket,subprocess,json,os,time
import class_comm
def auth(user_list):
    print("\033[31;1m欢迎登陆! 当前时间：%s\033[0m" % (
        time.strftime("%Y/%m/%d %H:%M:%S %A")))
    #用户账号密码字典
    user_list = user_list
    #创建统计用户登陆密码错误次数的空字典
    log_coun = {}
        #创建被锁定用户清单空列表
    lock_list = []
    coun = 0
        #将存放用户账密字典里的用户名提取出来，生成user_name用户列表
    user_name = user_list.keys()
        #提取账密字典里的用户名，并赋值数字0，生成一个用户登陆次数的字典
    for user_list_coun in  user_list.keys() :
        log_coun[user_list_coun] = 0
    addr = input("输入FTP服务器IP地址：")
    while True:
        log_name = str(input("请输入用户名："))
        #判断输入的用户是否在lock_list列表里
        if log_name in lock_list :
            print("此用户被锁定")
            break
        '''
        判断输入的用户密码是否正确，如果密码错误，给该用户错误次数加1.
        如累计次数到3，将该用户添加到禁止登陆的列表里
        '''
        if log_name in user_name :
            log_passwd = str(input("请输入密码："))
            if log_passwd == user_list[log_name] :
                print("登录成功！")
                subprocess.getoutput("mkdir %s"%log_name)
                user_com = class_comm.Ftp(log_name,addr)
                user_com.Client()
                break
            else :
                print("密码错误，请重新输入用户名密码.\n")
                coun += 1
                log_coun[log_name] += 1
                if log_coun[log_name] == 3 :
                    lock_list.append(log_name)
        else :
            print("用户名不存在，请确认用户名是否正确.\n")
            coun += 1
        #所有的错误次数超过4次，禁止继续尝试，程序退出
        if coun == 4 :
            print("错误次数太多，禁止继续尝试！")
            break
    return log_name