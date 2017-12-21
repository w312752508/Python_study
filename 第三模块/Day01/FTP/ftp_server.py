import subprocess,os
import socket
server = socket.socket()
server.bind(("localhost",30000))
server.listen()
print("服务开启中。。。")
con, addr = server.accept()
while True:
    data = con.recv(2000)
    if data.decode() =="exit":
        break
    elif "dir" in data.decode() :
        info = subprocess.getoutput(data.decode())
        if info:
            con.send(info.encode("utf-8"))
        else:
            con.send(("空目录，无文件").encode("utf-8"))
    else:
        subprocess.getoutput(data.decode())
print("服务关闭，程序退出！")
server.close()

