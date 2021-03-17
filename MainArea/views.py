from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User


from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import FormView, CreateView
from django.http import JsonResponse

from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import ContactForm, NewUserForm, UserProfileInfoForm
from ProxyChecker.forms import UrlStringFormView
# Forms Collection

# import der App aus dem ProxyChecker
from ProxyChecker.models import GoodProxy , ProxyStringUrl
from MainArea.models import UserProfileInfo
# import der App aus dem ProxyChecker

# Filter einbauen und Proxys sortieren
from .filters import ProxyFilter



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
    anonymitaet = ["Elite","High Anonymous","Transparent","Anonymous"]
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
    #print(proxys)
    return render(request,'home.html', {"ipList":proxys})
#   return HttpResponse('Hello, World!')



def like_button(request):
   ctx={"hello":"hello"}
   return render(request,"like/like_template.html",ctx)





def UserDashboard(request):
    # user = User.objects.get(id=request.user.id)
    print("user id ist",request.user.id)
    random.seed()
    goodProxys = GoodProxy.objects.all()
    #filter = FilmFilter(request.GET, queryset = films)
    Pcount= GoodProxy.objects.count()
    proxys=[]
    url_cForm = UrlStringFormView()
    url_strings = ProxyStringUrl.objects.all()
    proxyFilter = ProxyFilter(request.GET, queryset = goodProxys)
    try:
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
    except Exception as e:
        print(e)
        pass


    # Bereich um URLs in der DB zu speichern und ggf. zu chekchen Ajax Post-call
    if request.method == "POST" and request.is_ajax():
        form = UrlStringFormView(request.POST)
        if form.is_valid():
            user = request.user.id
            formUrl = form.cleaned_data['urlstring']
            form.save()
            return JsonResponse({"urlstring": formUrl}, status=200)
        else:
            errors = form.errors.as_json()
            return JsonResponse({"errors": errors}, status=400)
    #userProfile = UserProfileInfo.objects.get(user=User.o)



    return render(request,'userDashboard/dashboard0.html',{"ipList":proxys,
                                                        'gPcount':Pcount,
                                                        'countrys':"45664",
                                                        'save_url': url_cForm,
                                                        'url_strings':url_strings,
                                                        "proxyFilter":proxyFilter,
                                                        })

# https://www.pluralsight.com/guides/work-with-ajax-django
def login_request(request):
    #print("rendern! ")
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
    saved = False
    # https://medium.com/@himanshuxd/how-to-create-registration-login-webapp-with-django-2-0-fd33dc7a6c67

    if request.method == "POST":
        user_form = UserCreationForm(request.POST)
        profile_form = UserProfileInfoForm(request.POST,request.FILES)
        if user_form.is_valid():
            user = user_form.save()
            username = user_form.cleaned_data.get('username')
            profile = profile_form.save(commit=False)
            if profile_form.is_valid():
                profile.user = user
                for i in request.FILES:
                    print(i)
                if 'profile_pic' in request.FILES:
                    print('found it')
                    profile.profile_pic = request.FILES['profile_pic']
                else:
                    print("ProfilePic not founded!")
                print("Profile wird saved")
                profile.save()
                saved = True
            login(request, user)
            return redirect("main:login")
        else:
            print(user_form.errors,profile_form.errors)

    user_form = UserCreationForm
    profile_form = UserProfileInfoForm()
    return render(request = request,
                  template_name = "authTemplates/register.html",
                  context={"user_form":user_form,
                  'profile_form':profile_form,})


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

class SignUpView(CreateView):
    template_name = 'authTemplates/signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('main:dashboard')

    def form_valid(self, form):
        valid = super().form_valid(form)
        login(self.request, self.object)
        return valid
