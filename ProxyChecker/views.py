from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from . import models
from django.contrib.auth.models import User
import logging
from django.contrib import messages
from django.views.generic.edit import FormView
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from .src.checker import checkPROXY_DB, FarmProxysOS
from .src.ismyipbad import IsMyIpBad

from .forms import InputCsvForm, UrlStringFormView
# parts
# - show the current user geolocation in the dashboard
# - get Longtitude, Altitude and City from the Proxys

# https://medium.com/@arrosid/get-visitor-location-using-geoip2-in-django-32ad3d417115

from django.contrib.gis.geoip2 import GeoIP2
from pprint import pprint
#g = GeoIP2()
#result = g.city('213.136.89.190')
#pprint(result)




""" HELPS
https://www.techiediaries.com/resetting-django-migrations/
"""

def ProxyChecker(request):
    if request.method == 'GET':
        form = InputCsvForm()
    else:
        # A POST request: Handle Form Upload
        form = InputCsvForm(request.POST)  # Bind data from request.POST into a PostForm
        # If data is valid, proceeds to create a new post and redirect the user
        if form.is_valid():
            # FileUpload = forms.FileUpload()
            Textfield = form.cleaned_data['Textfield']
            # save to db
            user = User.objects.get(id=1) #TODO:: Die Proxy müssen immer zu dem eingellogten User eingetragen werden
            proxy = models.UserProxy.objects.create(user=user, protokol="Socks5", country=Textfield)
            proxy.save()
            #print(proxy.protokol)
            # return HttpResponseRedirect(reverse('post_detail',kwargs={'post_id': post.id}))

    form = {}
    form['form'] = InputCsvForm()
    return render(request, "ProxyChecker/Pchecker.html", form)



class URL_String_Upload(FormView):
    template_name = 'userDashboard/Dashboard.html'
    form_class = UrlStringFormView

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



def upload_csv(request):
    """
    https://pythoncircle.com/post/30/how-to-upload-and-process-the-csv-file-in-django/
    """
    if request.user.is_anonymous:
        anoymous = 2
        print(request.user.id,"\n\n\n")
        user = User.objects.get(pk=anoymous)
        data = {}
        if "GET" == request.method:
            return render(request, "ProxyChecker/Pchecker.html", data)
        # if not GET, then proceed
        try:
            csv_file = request.FILES["csv_file"]
            if not csv_file.name.endswith('.csv'):
                messages.error(request, 'File is not CSV type')
                return HttpResponseRedirect(reverse("ProxyChecker:PChecker"))
            # if file is too large, return
            if csv_file.multiple_chunks():
                messages.error(request, "Uploaded file is too big (%.2f MB)." % (csv_file.size / (1000 * 1000),))
                return HttpResponseRedirect(reverse("ProxyChecker:PChecker"))

                # loop over the lines and save them in db. If error , store as string and then display
            file_data = csv_file.read().decode("utf-8")
            lines = file_data.split("\n")
            for line in lines:
                    fields = line.split(":")
                    data_dict = {}
                    data_dict["ipaddress"] = fields[0]
                    data_dict["port"] = fields[1]
                    #data_dict["First name"] = fields[2]
                    #data_dict["Last name"] = fields[3]
                    #print( "\n" ,str(data_dict), "\n")
                    try:
                        proxy = models.UserProxy.objects.create(user=user,
                                                                ipAdress=data_dict['ipaddress'],
                                                                port=data_dict['port'])
                        proxy.save()
                        #form = EventsForm(data_dict) # <-----------------------
                        #if form.is_valid():
                        #    form.save()
                        #else:
                        #    logging.getLogger("error_logger").error(form.errors.as_json())
                    except Exception as e:
                        logging.getLogger("error_logger").error(repr(e))
                        pass
        except Exception as e:
                logging.getLogger("error_logger").error("Unable to upload file. " + repr(e))
                messages.error(request, "Unable to upload file. " + repr(e))
    else:

        print(request.user.id,"\n\n\n")
        user = User.objects.get(pk=request.user.id)
        data = {}
        if "GET" == request.method:
            return render(request, "ProxyChecker/Pchecker.html", data)
        # if not GET, then proceed
        try:
            csv_file = request.FILES["csv_file"]
            if not csv_file.name.endswith('.csv'):
                messages.error(request, 'File is not CSV type')
                return HttpResponseRedirect(reverse("ProxyChecker:PChecker"))
            # if file is too large, return
            if csv_file.multiple_chunks():
                messages.error(request, "Uploaded file is too big (%.2f MB)." % (csv_file.size / (1000 * 1000),))
                return HttpResponseRedirect(reverse("ProxyChecker:PChecker"))

                # loop over the lines and save them in db. If error , store as string and then display
            file_data = csv_file.read().decode("utf-8")
            lines = file_data.split("\n")
            for line in lines:
                    fields = line.split(":")
                    data_dict = {}
                    data_dict["ipaddress"] = fields[0]
                    data_dict["port"] = fields[1]
                    #data_dict["First name"] = fields[2]
                    #data_dict["Last name"] = fields[3]
                    #print( "\n" ,str(data_dict), "\n")
                    try:
                        proxy = models.UserProxy.objects.create(user=user,
                                                                ipAdress=data_dict['ipaddress'],
                                                                port=data_dict['port'])
                        proxy.save()
                        #form = EventsForm(data_dict) # <-----------------------
                        #if form.is_valid():
                        #    form.save()
                        #else:
                        #    logging.getLogger("error_logger").error(form.errors.as_json())
                    except Exception as e:
                        logging.getLogger("error_logger").error(repr(e))
                        pass
        except Exception as e:
                logging.getLogger("error_logger").error("Unable to upload file. " + repr(e))
                messages.error(request, "Unable to upload file. " + repr(e))


    # def background_process():
    #     print("\033[1;34m"+"process started")
    #     checkPROXY_DB(request)
    #     #FarmProxysOS()
    #     print("\033[1;34m"+"process finished")
    #def index(request):
    #    import threading
    #    t = threading.Thread(target=background_process, args=(), kwargs={})
    #    t.setDaemon(True)
    #    t.start()
    #    return HttpResponse("main thread content")

    # import threading
    # t = threading.Thread(target=background_process, args=(), kwargs={})
    # t.setDaemon(True)
    # t.start()

    return HttpResponseRedirect(reverse("main:dashboard"))

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


def BrowserLocation(request):


    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    #result = IsMyIpBad(ip)

    for i in request:
        print(i)

    device_type = ""
    browser_type = ""
    browser_version = ""
    os_type = ""
    os_version = ""
    if request.user_agent.is_mobile:
        device_type = "Mobile"
    if request.user_agent.is_tablet:
        device_type = "Tablet"
    if request.user_agent.is_pc:
        device_type = "PC"

    browser_type = request.user_agent.browser.family
    browser_version = request.user_agent.browser.version_string
    os_type = request.user_agent.os.family
    os_version = request.user_agent.os.version_string

    g = GeoIP2()
    location = g.city(ip)
    location_country = location["country_name"]
    location_city = location["city"]
    context = {"ip": ip,
                "device_type": device_type,
                "browser_type": browser_type,
                "browser_version": browser_version,
                "os_type":os_type,
                "os_version":os_version,
                "location_country": location_country,
                "location_city": location_city}
    return context
