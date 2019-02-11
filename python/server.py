import socket

s = socket.socket()
host = "0.0.0.0"
port = 12345
s.bind((host, port))
BACKLOG = 5

s.listen(BACKLOG)
while True:
    c, addr = s.accept()
    print("conn addr : ", addr)
    c.send("hello word")
    c.close()

import socket
s = socket.socket()
host = '0.0.0.0'
port = 12345
s.connect((host, port))
print(s.recv(1024))
s.close()