import socket
import sys
import socket,hashlib
a = 1
for i in range(40):
    client = socket.socket()
    client.connect(("localhost",10000))
    client.send(str(a).encode())
    a += 1
    data = client.recv(1024)
    print(data.decode())
    client.close()