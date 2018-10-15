import sys
from socket import *
serverHost = 'localhost'
serverPort = 50007

message = [b'Hello World!']

if len(sys.argv) > 1:
    serverHost = sys.argv[1]
    if len(sys.argv) > 2:
        message = (x.encode() for x in sys.argv[2:])

socketObj = socket(AF_INET, SOCK_STREAM)
socketObj.connect((serverHost, serverPort))

for l in message:
    socketObj.send(l)
    data = socketObj.recv(1024)
    print('Receive: ', data)

socketObj.close()