# -*- coding:utf-8 -*-
import select,socket,hashlib,json
def MD5(password):
    m = hashlib.md5()
    password = password.encode(encoding="utf-8")
    m.update(password)
    return m.hexdigest()

def Main():
    user_list = {"zhh":"zhh","lisi":"lisi"}
    HOST = 'localhost'
    PORT = 11111
    server = socket.socket()
    server.bind((HOST,PORT))
    server.listen(100)
    inputs = [server, ]
    outputs = []
    print("服务端启动。。。")
    while True:
        readable, writeable, exceptional = select.select(inputs, outputs, inputs)  # 监听事件列表，如果没有fd就绪，就一直阻塞在这
        for r in readable:
            if r is server:
                conn, addr = server.accept()
                print("建立新连接", addr)
                inputs.append(conn)
            else:
                try:
                    date = r.recv(1024)
                    date = json.loads(str(date,encoding="utf-8"))
                    if MD5(user_list[date[0]]) == date[1]:
                        r.send("true".encode())
                        Myserver(date[0])
                    else:
                        r.send("error".encode())
                except Exception as e:
                    print("客户端%s断开连接" % r)
                    inputs.remove(r)  # 从监听列表里移除异常连接
        for e in exceptional:
            if e in outputs:
                outputs.remove(e)
            inputs.remove(e)
            e.close()

if __name__ == "__main__":
    Main()