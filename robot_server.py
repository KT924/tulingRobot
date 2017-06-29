#!/usr/bin/python3
import socket
import json
import requests

#serversocket=socket.socket()
#host=socket.gethostname()
#port=9999
#serversocket.bind((host,port))
#serversocket.listen(5)

#while True:
#    clientsocket,addr=serversocket.accept()

#    print('连接地址：%s' % str(addr))
#    msg='欢迎使用图灵机器人！'+'\r\n'
#    clientsocket.send(msg.encode('utf-8'))
#    data=clientsocket.recv(1024)
#    print(data.decode('utf-8'))
#    clientsocket.close()
#    break
#serversocket.close()
class robot_server():
    def __init__(self,robotURL,key,host,port):
        self.robotURL=robotURL
        self.key=key
        self.host=host
        self.port=port
    def serverStart(self):
        serversocket=socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
        serversocket.bind((self.host,self.port))
        serversocket.listen(5)
        while True:
            clientsocket,addr=serversocket.accept()
            print('客户端地址： %s' % str(addr))
            msg='欢迎使用图灵机器人！\r\n'.encode('utf-8')
            clientsocket.send(msg)
            data=clientsocket.recv(2048)
            print(data.decode('utf-8'))
            result=self.apiHandle(text=data)
            #print(result)
            #print(data.decode('utf-8'))
            #clientsocket.send(msg)
            clientsocket.close()
            break
        serversocket.close()
    def apiHandle(self,text):
        data=text.decode('utf-8')
        requests.adapters.DEFAULT_RETRIES=5
        api = {'key': self.key, 'info': data, 'userid': 'abc12345'}
        data=json.dumps(api)
        result=requests.post(self.robotURL,data=data)
        print(result.text)


if __name__=='__main__':
    robot=robot_server('http://www.tuling123.com/openapi/api','b7fa799b04e1485dacadba67091d74ce',
                       'wkt',port=9999
                       )
    robot.serverStart()
