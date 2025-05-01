#!/usr/bin/env python
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(("data.pr4e.org", 80))

cmd = "GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n".encode()
print(f"cmd:\n{cmd}\n")

bytes_sent = mysock.send(cmd)  # is equal to len(cmd)

print(f"bytes_sent: {bytes_sent}")
print(f"bytes_sent==len(cmd): {bytes_sent == len(cmd)}\n")

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end="")

mysock.close()
