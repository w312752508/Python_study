import socket,subprocess,os,hashlib
server = socket.socket()
server.bind(("0.0.0.0",20000))
server.listen()
print("服务端启动，接收信息中")
while True:
    conn,addr = server.accept()
    print("新客户端接入")
    while True:
        data = conn.recv(1024)
        if data.decode() == "exit":
            print("客户端退出，等待新客户端接入")
            break
        else:
            if "get" in data.decode():
                data_in = data.decode().split()
                if os.path.isfile(data_in[1].strip()):
                    print((data_in[1].strip()))
                    f = open((data_in[1]),"rb")
                    m = hashlib.md5()
                    file_size = os.stat(data_in[1]).st_size
                    conn.send(str(file_size).encode())
                    conn.recv(1024)
                    for line in f:
                        m.update(line)
                        conn.send(line)
                    conn.send(m.hexdigest().encode())
                    f.close()
            else:
                info = subprocess.getoutput(data.decode())
                conn.send(str(len(info.encode())).encode("utf-8"))
                client_ack = conn.recv(1024)
                conn.send(info.encode("utf-8"))
server.close()
