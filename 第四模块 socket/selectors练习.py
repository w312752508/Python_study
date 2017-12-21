import selectors
import socket
sock = socket.socket()
sel = selectors.DefaultSelector()
sock.bind(("localhost",10000))
sock.listen(1000)
sock.setblocking(0)
def acc(sock,mask):
    conn,addr = sock.accept()
    conn.setblocking(0)
    sel.register(conn,selectors.EVENT_READ,read)
def read(conn,mask):
    try:
        date = conn.recv(1024)
        if date:
            print("收到信息:%s"%date)
            conn.send(date)
            print("send done")
    except Exception as e:
        print("连接断开：",conn)
        sel.unregister(conn)
        conn.close()

sel.register(sock,selectors.EVENT_READ,acc)
print("服务已启动")
while True:
    events = sel.select()
    for key,mask in events:
        callback = key.data
        callback(key.fileobj,mask)
