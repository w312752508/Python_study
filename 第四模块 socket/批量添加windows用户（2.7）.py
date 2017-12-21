# encoding:utf-8
import os,sys,random
from ftplib import FTP
# sys.path.append(b"c:\easyops\python")

def f_pwd():  #生成随机密码
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
        if False in jud_all:
            continue
        else:
            return check_num
            break

def ftp_load(): #从FTP下周用户列表
    ftp=FTP()
    ftp.connect("10.253.1.76","21")
    ftp.login("zhaohai","zhaohai")
    ftp.cwd("del_user")
    bufsize=1024
    filename = "add_name_list.txt"
    del_list = open(filename,"wb").write
    ftp.retrbinary("RETR add_name_list.txt",del_list,bufsize)
    ftp.set_debuglevel(0)
    ftp.quit()

def add_user():
    with open("add_name_list.txt", "rb") as f_d:
        f_d.seek(3)
        for i in f_d:
            i_list = i.split(",")
            pwd = f_pwd()
            os.popen("net user %s %s /add /fullname:%s"
                     %(i_list[0].strip().decode("utf-8").encode("gbk"),pwd.encode("gbk"),i_list[1].strip().decode("utf-8").encode("gbk")))
            os.popen('net localgroup "Remote Desktop Users" %s /add'
                     %i_list[0].strip().decode("utf-8").encode("gbk"))
            os.popen("net user %s /logonpasswordchg:yes"
                     %i_list[0].strip().decode("utf-8").encode("gbk"))
            print "新增用户%s"%i_list[0].strip(),"初始密码 %s"%pwd
ftp_load()
add_user()