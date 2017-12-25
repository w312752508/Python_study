import threading,socket,queue
semaphore = threading.BoundedSemaphore(5) #限制最大线程数
q = queue.Queue(maxsize=100) #接收客户端信息
lock = threading.Lock()
client_list = [["localhost",20000],
               ["localhost",20000],
               ]

def socket_req(cmd,addr,port):
    client = socket.socket()
    client.connect((addr, port))
    client.send(cmd.encode("utf-8"))
    data_size = client.recv(1024)
    rec_size = 0
    data_rec = b""
    client.send(b"1")
    while rec_size < int(data_size.decode()):
            data = client.recv(1024)
            rec_size += len(data)
            data_rec += data
    q.put(data_rec.decode())
    client.close()

def run(cmd,addr,port):
    lock.acquire()
    semaphore.acquire()
    socket_req(cmd,addr,port)
    semaphore.release()
    lock.release()

def nwehost_add():
    server = socket.socket()
    server.bind(("localhost", 10000))
    server.listen()
    print("服务端启动，接收信息中")
    while True:
        conn, addr = server.accept()

def _cmd():
    while True:
        cmd = input(">:")
        if len(cmd) == 0:
            continue
        elif cmd == "exit":
            break
        else:
            for i in client_list :
                addr,port = i[0],i[1]
                t = threading.Thread(target=run, args=(cmd,addr,port))
                t.setDaemon(True)
                t.start()
            for i in range(len(client_list)):
                print(q.get())

if __name__ == "__main__":

    _cmd()