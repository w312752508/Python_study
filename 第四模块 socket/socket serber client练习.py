import socket
import sys
import socket,hashlib
client = socket.socket()
client.connect(("localhost",10000))
while True:
    a = input(">:")
    client.send(a.encode())
    data = client.recv(1024)
    print(data.decode())
    client.close()