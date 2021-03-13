from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from . import models
from django.contrib.auth.models import User
from .forms import InputForm
import logging
from django.contrib import messages

from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from .src.checker import checkPROXY_DB, FarmProxysOS
""" HELPS
https://www.techiediaries.com/resetting-django-migrations/
"""

def ProxyChecker(request):
    if request.method == 'GET':
        form = InputForm()
    else:
        # A POST request: Handle Form Upload
        form = InputForm(request.POST)  # Bind data from request.POST into a PostForm
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
    form['form'] = InputForm()
    return render(request, "ProxyChecker/Pchecker.html", form)


def upload_csv(request):

    """
    https://pythoncircle.com/post/30/how-to-upload-and-process-the-csv-file-in-django/
    """
    print(request.user.id,"\n\n\n")
    user = User.objects.get(id=request.user.id)
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


    def background_process():
        print("\033[1;34m"+"process started")
        checkPROXY_DB(request)
        #FarmProxysOS()
        print("\033[1;34m"+"process finished")

    #def index(request):
    #    import threading
    #    t = threading.Thread(target=background_process, args=(), kwargs={})
    #    t.setDaemon(True)
    #    t.start()
    #    return HttpResponse("main thread content")


    import threading
    t = threading.Thread(target=background_process, args=(), kwargs={})
    t.setDaemon(True)
    t.start()
    #p = threading.Thread(target=FarmProxysOS, args=(), kwargs={})
    #p.setDaemon(True)
    #p.start()


    return HttpResponseRedirect(reverse("main:dashboard"))
