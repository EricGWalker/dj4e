#!/usr/bin/env python
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(("127.0.0.1", 9000))
cmd = "GET http://127.0.0.1/romeo.txt HTTP/1.0\r\n\r\n".encode()
_ = mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if not data:
        break
    print(data.decode(), end="")

mysock.close()
