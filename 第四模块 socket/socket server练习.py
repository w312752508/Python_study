import socketserver
class MyTcpHandler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            self.data = self.request.recv(1024)
            print("收到信息，处理中")
            self.request.sendall(self.data.upper())
            print("处理完毕，发送完成！")

if __name__ == "__main__":
    host,port = "0.0.0.0",20000
    server = socketserver.ThreadingTCPServer((host,port),MyTcpHandler)
    print("接收数据中。。。。")
    server.serve_forever()