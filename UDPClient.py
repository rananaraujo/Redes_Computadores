from socket import *
import datetime
import time


serverName = 'localhost'
port = 2014
Csocket = socket(AF_INET, SOCK_DGRAM)
data = ' ping'


LastPing = 10
count = 0
Csocket.settimeout(1)
   

while count  < LastPing:
        
    count = count + 1
    startTime = time.time()
    print("O tempo atual eh " , startTime," e essa eh a menssagem " , count)
    Csocket.sendto(data, (serverName, port))

    try:
        newData, clientAddress = Csocket.recvfrom(1024)
        RTT = ((time.time()) - startTime)
        print (newData)
        print ("Tempo de resposta", RTT)
    except timeout:
        print(" Solicitacao expirada ")
    except Exception as e:
        print e
print ("Progama finalizado")
