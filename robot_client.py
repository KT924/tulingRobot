#！/usr/bin/python3

import socket

client=socket.socket()

client.connect(('wkt',9999))
msg=client.recv(1024)
client.send('你好'.encode('utf-8'))
client.close()
print(msg.decode('utf-8'))