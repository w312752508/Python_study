# -*- coding:utf-8 -*-
import socket,os
import time,json,hashlib

DIR = os.path.dirname(os.path.abspath(__file__))
DIR = DIR.replace('core','Folder/')
HOST = 'localhost'
PORT = 10000

# def ls_Method(s):
#     s.send("Begin!")
#     data = ''
#     while True:
#         buffer = s.recv(1024)
#         if buffer == 'Exit!':
#             break
#         if not buffer:
#             print ("服务器传输错误！")
#             return
#         data += buffer
#     print (data)
#
# def put_Method(s,action,filename):
#     if os.path.exists(DIR+filename) and os.path.isdir(DIR+filename) == False:
#         with open(DIR+filename,'r') as f:
#             data = f.read()
#         data_size = len(data)
#         s.send(str(data_size))
#         if s.recv(1024) == 'OK!':
#             s.send(filename)
#             if s.recv(1024) == 'OK!':
#                 print ("文件开始上传，请稍后...")
#                 with open(DIR+filename,'r') as f:
#                     Num = None
#                     data = ''
#                     while True:
#                         buffer = f.read(1024)
#                         if not buffer:
#                             s.send("Exit!")
#                             break
#                         s.send(buffer)
#                         data += buffer
#                         Num = download_Progress(data_size, len(data), Num)
#                 if s.recv(1024) == 'OK!':
#                     print ("上传成功！磁盘配额剩余{0}M".format(s.recv(1024)))
#                 else:
#                     print ("文件传输有损，请重新上传！")
#             else:
#                 print ("不能上传！服务器上已有重名的文件")
#         else:
#             print ("磁盘配额已满，请清理磁盘空间！")
#     else:
#         s.send("False!")
#         print ("上传失败，没有这个文件或目标是个文件夹")
#
# def get_Method(s,action,filename):
#     s.send(filename)
#     print ("正在下载，请等待...")
#     data = ''
#     data_size = s.recv(1024)
#     if data_size == "Flase!":
#         print ("下载失败！服务器没有找到或目标是个文件夹")
#         return
#     data_size = int(data_size)
#     Num = None
#     while True:
#         buffer = s.recv(1024)
#         if not buffer :
#             print ("文件损坏，请重新下载！")
#             break
#         data += buffer
#         Num = download_Progress(data_size,len(data),Num)
#         if data_size == len(data):
#             with open(DIR + filename, 'w') as f:
#                 f.write(data)
#                 print ("下载成功！")
#                 break
#
# def cd_Method(s,action,filename):
#     s.send(filename)
#     re = s.recv(1024)
#     if re == 'OK!':
#         print ("命令执行成功！")
#     elif re == 'NULL!':
#         print ("已到根目录，不能继续返回！")
#     else:
#         print ("目录没有找到！")
#
# def mkdir_Method(s,action,filename):
#     s.send(filename)
#     if s.recv(1024) == 'OK!':
#         print ("目录创建成功！")
#     else:
#         print ("已有同名目录或文件！")
#
# def rm_Method(s,action,filename):
#     s.send(filename)
#     re = s.recv(1024)
#     if re == "OK!":
#         print ("删除成功！磁盘配额剩余{0}M".format(s.recv(1024)))
#     elif re == "DIR!":
#         while True:
#             decide = input("您选择的目标是个文件夹，是否递归删除（y/n）：")
#             if decide == 'y':
#                 s.send("OK!")
#                 re = s.recv(1024)
#                 if re == "OK!":
#                     print ("删除成功，磁盘配额剩余{0}M".format(s.recv(1024)))
#                     break
#                 else:
#                     print ("删除失败，原因未知！")
#                     break
#             elif decide == 'n':
#                 s.send("False!")
#                 break
#             else:
#                 print ("您的输入有误！")
#     else:
#         print ("没有这个文件")
#
# def download_Progress(size_total,size,Num):
#     num = size * 100 / size_total
#     if Num == None:
#         print ("\r%d" %num)
#         time.sleep(0.01)
#         return num
#     elif num == Num:
#         return num
#     else:
#         print ("\r%d" % num,)
#         time.sleep(0.01)
#         return num
#
#
#
#
def File_transfer(s):
    while True:
        command = input("请输入你想执行的命令>>")
        if not command:
            continue
        if command.lower().strip() == 'help':
            text = """请用'put'+'空格'+'文件名'的格式上传文件
                    请用'get'+'空格'+'文件名'的格式下载文件
                    请用'cd'+'空格'+'目录名'的格式进入家目录下的子文件夹
                    请用'cd'+'空格'+'..'的格式返回上级目录
                    请用'mkdir'+'空格'+'目录名'的格式进入家目录的文件夹
                    请用'rm'+'空格'+'文件名／目录名'的格式删除家目录下的文件
                    输入'ls'查看用户服务器家目录"""
            print (text)
            continue
        try:
            action,filename = command.strip().split()
            action = action.lower()
        except:
            if command.lower().strip() == 'ls':
                s.send('ls'.encode())
                print ("正在查询，请稍后...")
                if str(s.recv(1024),encoding="utf-8") == 'OK':
                    continue
                    # ls_Method(s)
            else:
                print ("您的输入有误!输入help查看帮助文档")
                continue
        else:
            s.send(action)
            if s.recv(1024) == 'OK!':
                eval(action+'_Method')(s,action,filename)
            else:
                print ("您的输入有误！输入help查看帮助文档")
def MD5(password):
    m = hashlib.md5()
    password = password.encode(encoding="utf-8")
    m.update(password)
    return m.hexdigest()

def Login(s):
    while True:
        name = input("请输入你的登陆名：").strip()
        password = input("请输入你的密码：").strip()
        if not name or not password:
            print ("用户名和密码不能为空！")
            continue
        password = MD5(password)
        data = [name,password]
        data = json.dumps(data)
        s.send(bytes(data,encoding="utf-8"))
        r_data =s.recv(1024)
        r_data = str(r_data,encoding="utf-8")
        if r_data == 'true':
            print ("登陆成功！欢迎使用FTP服务！")
            File_transfer(s)
            s.close()
            break
        else:
            print ("用户登陆失败！")


def Main():
    s = socket.socket()
    s.connect((HOST, PORT))
    Login(s)
if __name__ == "__main__":
    Main()