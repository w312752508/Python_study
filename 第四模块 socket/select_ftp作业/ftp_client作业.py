# -*- coding:utf-8 -*-
import socket,os
import time,json,hashlib

DIR = os.path.dirname(os.path.abspath(__file__))
DIR = DIR.replace('core','Folder/')
HOST = 'localhost'
PORT = 11111


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