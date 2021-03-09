from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import NewUserForm
from django.contrib.auth import logout, authenticate, login
from ProxyChecker.models import GoodProxy


import datetime
import random
import socket
import struct

def home_page_view(request):
    random.seed()
    goodProxys = GoodProxy.objects.all()
    proxys=[]
    defaultPorts = [80, 8080]
    onlineStatus = ["yes","no"]
    Protokoll = ["Socks5","Socks4","Http","Https"]
    anonymitaet =["Elite","High Anonymous","Transparent","Anonymous"]
    for proxy in goodProxys:
        proxys.append([
                        str(random.randint(1,10))+" min",
                        proxy.ipAdress, # ipAdresse
                        str(proxy.port), # port
                        proxy.country,
                        str(random.randint(40,100)),
                        int(proxy.latenz),
                        "online",
                        proxy.protokol,
                        proxy.anonymitaetsLevel
                        ])
        #ip = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
        #port = str(defaultPorts[random.randint(0,1)])
    print(proxys)
    return render(request,'home.html', {"ipList":proxys})
#   return HttpResponse('Hello, World!')

def UserDashboard(request):
    random.seed()
    goodProxys = GoodProxy.objects.all()
    proxys=[]
    for proxy in goodProxys:
        proxys.append([
                        str(random.randint(1,10))+" min",
                        proxy.ipAdress, # ipAdresse
                        str(proxy.port), # port
                        proxy.country,
                        str(random.randint(40,100)),
                        int(proxy.latenz),
                        "online",
                        proxy.protokol,
                        proxy.anonymitaetsLevel
                        ])
        #ip = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
        #port = str(defaultPorts[random.randint(0,1)])
    return render(request,'userDashboard/charts-chartjs.html',{"ipList":proxys})

def login_request(request):
    print("rendern! ")
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                print("Sie sind eingelogt")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()

    return render(request = request,
                    template_name = "authTemplates/login.html",
                    context={"form":form})

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("main:home")

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            return redirect("main:login")

        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

            return render(request = request,
                          template_name = "authTemplates/register.html",
                          context={"form":form})

    form = UserCreationForm
    return render(request = request,
                  template_name = "authTemplates/register.html",
                  context={"form":form})
