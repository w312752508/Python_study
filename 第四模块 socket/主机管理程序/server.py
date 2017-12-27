import threading,socket,queue,os
semaphore = threading.BoundedSemaphore(20)
lock = threading.Lock()
q = queue.Queue()
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
def _cmd():
    print("主机总数：%s" % len(client_list))
    for i in client_list:
        print("Host_IP:%s Prot:%s" % (i[0], i[1]))

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