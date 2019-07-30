# -*- coding: utf-8 -*-
from socket import *
import random

socket = socket(AF_INET, SOCK_DGRAM )
socket.bind(('', 2014))
print("I will be waiting on port" , 2014)

while True:
        RandNum = random.randint(0,10)
        data , clientAddress = socket.recvfrom(1024)
        newData =  data.upper()



        if RandNum < 4:
            print ("packet lost")
            continue

        socket.sendto(newData, clientAddress)
