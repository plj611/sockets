from socket import *
myHost = ''
myPort = 50007

sockObj = socket(AF_INET, SOCK_STREAM)
sockObj.bind((myHost, myPort))
sockObj.listen(5)

while True:
    connection, address = sockObj.accept()
    print('Connected by: ', address)
    while True:
        data = connection.recv(1024)
        if not data: break
        connection.send(b'Echo: ' + data)
    connection.close()