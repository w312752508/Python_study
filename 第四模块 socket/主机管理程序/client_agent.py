import socketserver,os
class MyTcpHandler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            data = self.request.recv(1024)
            data = os.popen(data.decode()).read()
            data_size = str(len(data.encode()))
            self.request.send(data_size.encode())
            self.request.recv(8)
            self.request.send(data.encode())
            break

if __name__ == "__main__":
    host,port = "0.0.0.0",20000
    server = socketserver.ThreadingTCPServer((host,port),MyTcpHandler)
    print("接收数据中。。。。")
    server.serve_forever()