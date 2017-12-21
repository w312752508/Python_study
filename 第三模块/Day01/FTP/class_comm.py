import socket,os
class Ftp(object):
    def __init__(self,user,addr):
        self.user = user
        self.addr = addr
    def Client(self):
        client = socket.socket()
        client.connect((self.addr,30000))
        while True:
            a = input(">:")
            if a == "exit":
                client.send(a.encode("utf-8"))
                break
            elif a == "dir":
                client.send(("dir /B %s"%self.user).encode("utf-8"))
                data = client.recv(2000)
                print(data.decode())
            elif not a:
                continue
            elif "put" in a:
                b = a.replace("put", "copy")
                client.send(("%s %s" % (b,self.user)).encode("utf-8"))
            elif "get" in a :
                b = a.replace("get ", "copy %s\\"%self.user)
                client.send(b.encode("utf-8"))
            elif "rm" in a :
                b = a.replace("rm", "del /f /s /q")
                client.send(("%s" %b).encode("utf-8"))
            else:
                print("\033[31;1m命令不存在，请重新输入\033[0m")
                continue
        client.close()