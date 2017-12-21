import socket,hashlib
client = socket.socket()
client.connect(("localhost",20000))
while True:
    a = input(">:")
    if len(a) == 0 :continue
    elif a == "exit":
        client.send(a.encode("utf-8"))
        break
    elif "get" in a :
        client.send(a.encode("utf-8"))
        data_size = client.recv(1024)
        client.send("收到".encode())
        data_len = 0
        data_rec = b""
        filename = a.split()[1]
        f = open(filename+"_new","wb")
        m = hashlib.md5()
        while data_len < int(data_size.decode()):
            sy_size = int(data_size.decode()) - data_len
            if sy_size > 1024:
                data = client.recv(1024)
            else:
                data = client.recv(sy_size)
            data_len += len(data)
            data_rec += data
            m.update(data)
            #加密操作自带有粘包效果，每次加密相当于加密(data += data)的内容，并不是单单只加密本次循环中data的值

            f.write(data)
        new_filemd5 = m.hexdigest()
        f.close()
        print("接收完成，原文件大小：%s,收到大小：%s"%(data_size,data_len))
        mds_server = client.recv(1024)
        print("原文件md5值：%s，\n新文件md5值：%s"%(mds_server,new_filemd5))

    else:    
        client.send(a.encode("utf-8"))
        data_size = client.recv(1024)
        client.send("收到".encode())
        data_len = 0
        data_rec = b""
        while data_len < int(data_size.decode()):
            data = client.recv(1024)
            data_len += len(data)
            data_rec += data
        else:
            print(data_rec.decode())