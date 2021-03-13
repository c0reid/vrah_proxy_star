from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.generic.edit import CreateView
from django.urls import reverse, reverse_lazy
from django.http import JsonResponse
from .forms import ContactForm

from .forms import NewUserForm

from ProxyChecker.models import GoodProxy

import datetime
import random
import socket
import struct



from django.views.generic.edit import FormView


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
        proxys.append([str(random.randint(1,10))+" min",
                        proxy.ipAdress, # ipAdresse
                        str(proxy.port), # port
                        proxy.country,
                        str(random.randint(40,100)),
                        int(proxy.latenz),
                        "online",
                        proxy.protokol,
                        proxy.anonymitaetsLevel])
        #ip = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
        #port = str(defaultPorts[random.randint(0,1)])
    return render(request,'userDashboard/dashboard0.html',{"ipList":proxys,
                                                        'gPcount':goodProxys.count(),
                                                        'countrys':"45664"})

# https://www.pluralsight.com/guides/work-with-ajax-django
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
                return redirect('/dashboard')
                # return redirect('/dashboard')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()

    return render(request = request,
                    template_name = "authTemplates/login3.html",
                    context={"form":form})

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("main:dashboard")

def ajax_view(request):
    if request.method == "POST":
        print(request.POST)
        data = {
            "msg": "Data has been POSTED!",
        }
        return JsonResponse(data)
    else:
        data = {
            "msg": "It worked!!",
        }
        return JsonResponse(data)

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


def validate_username(request):
    """Check username availability"""
    username = request.GET.get('username', None)
    response = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(response)

def contact_form(request):
    form = ContactForm()
    if request.method == "POST" and request.is_ajax():
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            form.save()
            return JsonResponse({"name": name}, status=200)
        else:
            errors = form.errors.as_json()
            return JsonResponse({"errors": errors}, status=400)

    return render(request, "contacts/contacts.html", {"form": form})

class ContactFormView(FormView):
    template_name = 'contacts/contacts.html'
    form_class = ContactForm

    def form_valid(self, form):
        """
        If the form is valid return HTTP 200 status
        code along with name of the user
        """
        name = form.cleaned_data['name']
        form.save()
        return JsonResponse({"name": name}, status=200)

    def form_invalid(self, form):
        """
        If the form is invalid return status 400
        with the errors.
        """
        errors = form.errors.as_json()
        return JsonResponse({"errors": errors}, status=400)



@login_required
def home(request):
    return render(request, 'home.html')


class SignUpView(CreateView):
    template_name = 'authTemplates/signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('main:dashboard')

    def form_valid(self, form):
        valid = super().form_valid(form)
        login(self.request, self.object)
        return valid


def validate_username(request):
    """Check username availability"""
    username = request.GET.get('username', None)
    response = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(response)
