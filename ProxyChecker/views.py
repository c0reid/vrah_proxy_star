from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login


import datetime
import random
import socket
import struct
# Create your views here.
def ProxyChecker(request):
    random.seed()
    proxys=[]
    defaultPorts = [80, 8080]
    onlineStatus = ["yes","no"]
    Protokoll = ["Socks5","Socks4","Http","Https"]
    anonymitaet =["Elite","High Anonymous","Transparent","Anonymous"]
    for i in range(150):
        proxys.append([
                        str(random.randint(1,10))+" min",
                        str(defaultPorts[random.randint(0,1)]),
                        socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff))),
                        str(random.randint(1,4))+"."+ str(random.randint(0, 99)),
                        str(random.randint(0,100)),
                        str(random.randint(0,2))+"."+str(random.randint(0, 99)),
                        str(onlineStatus[random.randint(0,1)]),
                        str(Protokoll[random.randint(0,3)]),
                        str(anonymitaet[random.randint(0,3)])
                        ]
                        )

        #ip = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
        #port = str(defaultPorts[random.randint(0,1)])

    print(proxys)


    return render(request,'ProxyChecker/Pchecker.html', {"ipList":proxys})
