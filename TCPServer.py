#import socket module
from socket import *
import sys # para terminar o programa
sock = socket(AF_INET, SOCK_STREAM)
server_address = ('127.0.0.1', 3000)
sock.bind(server_address)
sock.listen(1)

while True:
    print('Ready to serve...')
    connectionSocket, addr = sock.accept()
    try:
        message = connectionSocket.recv(1024)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata =  f.read()
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n")
        

        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i])
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n")
    connectionSocket.
    close()
serverSocket.close()
sys.exit()#Termina o programa depois de enviar os dados