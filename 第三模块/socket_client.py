import socket

client = socket.socket()
client.connect(("localhost", 30000))
while True:
    a = input(">:")
    if a == "exit":
        client.send(a.encode("utf-8"))
        break
    elif a == "dir":
        b = input("输入目录名:")
        # c = "dir %s"%b
        # print(c)
        client.send(("dir %s"%b).encode("utf-8"))
        data = client.recv(2000)
        print(data.decode())
    elif not a:
        continue
    elif "get" in a or "rm" in a or "put" in a :
        client.send(a.encode("utf-8"))
    else:
        print("\033[31;1m命令不存在，请重新输入\033[0m")
        continue
client.close()