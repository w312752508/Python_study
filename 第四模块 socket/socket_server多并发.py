import select,socket,queue
server = socket.socket()
server.bind(("localhost", 20000))
server.listen(1000)
inputs = [server,] #监控列表里一定要有对象，如果为空列表，程序会报错。因初始监控列表还未添加对象
# 所以手动添加监听server主程序，正好也避免了初次运行列表为空报错
outputs = []
print("服务端启动。。。")
while True:
    readable,writeable,exceptional = select.select(inputs,outputs,inputs) #监听事件列表，如果没有fd就绪，就一直阻塞在这
    for r in readable:
        if r is server:
            conn,addr = server.accept()
            print("建立新连接",addr)
            inputs.append(conn)
        else:
            try:
                date = r.recv(1024)
                print("收到信息：",date)
                r.send(date)
                print("send done")
            except Exception as e :
                print("客户端%s断开连接"%r)
                inputs.remove(r) #从监听列表里移除异常连接
    for e in exceptional:
        if e in outputs:
            outputs.remove(e)
        inputs.remove(e)
        e.close()
