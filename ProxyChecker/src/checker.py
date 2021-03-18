from proxy_checker import ProxyChecker
from ProxyChecker.models import UserProxy, GoodProxy, BadProxy
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Count, Max
from django.utils import timezone
from django.contrib.auth.models import User
from ProxyChecker.src.urlfarmer import urlfarmer


#Colours
red="\033[1;31m"
green="\033[1;32m"
yellow="\033[1;33m"
blue="\033[1;34m"
defcol = "\033[0m"


from background_task import background


# https://django-background-tasks.readthedocs.io/en/latest/
# notify_user(user.id, schedule=90) # 90 seconds from now
# notify_user(user.id, schedule=timedelta(minutes=20)) # 20 minutes from now
# notify_user(user.id, schedule=timezone.now()) # at a specific time


@background(schedule=10, queue='Proxy-valid')
def notify_user():
    # lookup user by id and send them a message
    #user = User.objects.get(pk=user_id)
    print("Bachground task from django with schedule")
    #user.email_user('Here is a notification', 'You have been notified')



def getDBProxys(request_userid):
    notify_user()
    dbProxys = UserProxy.objects.all().filter(user=request_userid.user.id)
    testProxy = []
    for i in dbProxys:
        testProxy.append(i.ipAdress+":"+str(i.port))
        print(i.id, i.ipAdress+":"+str(i.port))
    #print(testProxy)
    print("Es sind:", len(dbProxys), "Datensätze")
    return testProxy

def LoadProxys():
    pass

def CleanUpMainProxyDatabase(Request):
    # urlfarmer.FarmProxys()
    unique_fields = ['ipAdress', 'port']
    print(UserProxy.objects.values(*unique_fields).count())
    duplicates = (
        UserProxy.objects.values(*unique_fields)
        .order_by()
        .annotate(max_id=Max('id'), count_id=Count('id'))
        .filter(count_id__gt=1)
    )

    for duplicate in duplicates:
        (
            UserProxy.objects
            .filter(**{x: duplicate[x] for x in unique_fields})
            .exclude(id=duplicate['max_id'])
            .delete()
        )
    print(UserProxy.objects.values(*unique_fields).count())
    print("\033[1;32mMainDatabase von Duplikaten befreit")

def FarmProxysOS():
    import proxyscrape
    from proxyscrape import create_collector, get_collector
    print("Starting scraping")
#    collector = create_collector('my-collector', ['socks4', 'socks5'])
    collector = proxyscrape.create_collector('my-collector', 'http')  # Create a collector for http resources
    proxies = collector.get_proxies()
    print("Stoping scraping")
    for i in proxies:
        print(i)

def checkPROXY_DB(Request):
    ###################
    #######################
    if Request.user.is_anonymous:
        userid = 1
        CleanUpMainProxyDatabase(Request)
        print("Userid:", userid)
        user = User.objects.get(id=userid)
        dbProxys = UserProxy.objects.all().filter(user=user)
        badProxy = BadProxy.objects.all().filter(user=user)
        goodProxys = GoodProxy.objects.all().filter(user=user)
        #testProxy = []
        checker = ProxyChecker()
        for i in dbProxys:
            # ProxyId ran holen
            proxy = dbProxys.get(id=i.id)
            print(proxy)
            # ist der Proxy in der BadProxy List =
            badProxyCount=BadProxy.objects.filter(ipAdress=i.ipAdress,port=i.port).count()
            goodProxyCount=GoodProxy.objects.filter(ipAdress=i.ipAdress,port=i.port).count()
            print(badProxyCount,goodProxyCount)
            if badProxyCount == 0 and goodProxyCount == 0:
                print(defcol+"Proxy not in Bad and Good -Proxylist\nChecking Proxy:", str(i.id), i.ipAdress+":"+str(i.port))
                tesstproxy=checker.check_proxy(i.ipAdress+":"+str(i.port))
                if tesstproxy == False:
                    try:
                        newbadProxy = badProxy.create(user_id=userid,
                                                        ipAdress=i.ipAdress,
                                                        port=i.port)
                        newbadProxy.save()
                        print(red+"Bad ProxyId:{}:added to BadProxys".format(i.id))

                        #Aktualsiere Badproxys
                        badProxy = BadProxy.objects.all().filter(user=userid)
                    except ObjectDoesNotExist as DoesNotExist:
                        print(red+"Fehler!!! ObjectDoesNotExist ")
                else:
                    try:
                        if goodProxyCount == 0:
                            newgoodProxy = goodProxys.create(user_id=userid,
                                                            ipAdress=i.ipAdress,
                                                            port=i.port,
                                                            protokol = tesstproxy['protocols'][0],
                                                            anonymity=tesstproxy["anonymity"],
                                                            latenz=tesstproxy["timeout"],
                                                            countryCode=tesstproxy["country_code"],
                                                            country=tesstproxy["country"],
                                                            )
                            newgoodProxy.save()
                            print(green+"Proxy mit der ID:",i.id,"wurde Validiert und zu GoodProxys hinzugefügt!!")

                    except ObjectDoesNotExist as DoesNotExist:
                        print("Fehler!!! ObjectDoesNotExist")
            else:
                print("Ist in der GoodProxy or BadProxy -list!")
        print("alle Proxys wurden getestet!!!")

    else:
        text = f"""
        Some attributes of the HttpRequest object:

        scheme: {Request.scheme}
        path:   {Request.path}
        method: {Request.method}
        GET:    {Request.GET}
        user:   {Request.user}
        """
        print(text)
        userid = int(Request.user.id)
        CleanUpMainProxyDatabase(Request)
        print("Userid:", userid)
        user = User.objects.get(id=userid)
        dbProxys = UserProxy.objects.all().filter(user=user)
        badProxy = BadProxy.objects.all().filter(user=user)
        goodProxys = GoodProxy.objects.all().filter(user=user)
        #testProxy = []
        checker = ProxyChecker()
        for i in dbProxys:
            # ProxyId ran holen
            proxy = dbProxys.get(id=i.id)
            print(proxy)
            # ist der Proxy in der BadProxy List =
            badProxyCount=BadProxy.objects.filter(ipAdress=i.ipAdress,port=i.port).count()
            goodProxyCount=GoodProxy.objects.filter(ipAdress=i.ipAdress,port=i.port).count()
            print(badProxyCount,goodProxyCount)
            if badProxyCount == 0 and goodProxyCount == 0:
                print(defcol+"Proxy not in Bad and Good -Proxylist\nChecking Proxy:", str(i.id), i.ipAdress+":"+str(i.port))
                tesstproxy=checker.check_proxy(i.ipAdress+":"+str(i.port))
                if tesstproxy == False:
                    try:
                        newbadProxy = badProxy.create(user_id=userid,
                                                        ipAdress=i.ipAdress,
                                                        port=i.port)
                        newbadProxy.save()
                        print(red+"Bad ProxyId:{}:added to BadProxys".format(i.id))

                        #Aktualsiere Badproxys
                        badProxy = BadProxy.objects.all().filter(user=userid)
                    except ObjectDoesNotExist as DoesNotExist:
                        print(red+"Fehler!!! ObjectDoesNotExist ")
                else:
                    try:
                        if goodProxyCount == 0:
                            newgoodProxy = goodProxys.create(user_id=userid,
                                                            ipAdress=i.ipAdress,
                                                            port=i.port,
                                                            protokol = tesstproxy['protocols'][0],
                                                            anonymity=tesstproxy["anonymity"],
                                                            latenz=tesstproxy["timeout"],
                                                            countryCode=tesstproxy["country_code"],
                                                            country=tesstproxy["country"],
                                                            )
                            newgoodProxy.save()
                            print(green+"Proxy mit der ID:",i.id,"wurde Validiert und zu GoodProxys hinzugefügt!!")

                    except ObjectDoesNotExist as DoesNotExist:
                        print("Fehler!!! ObjectDoesNotExist")
            else:
                print("Ist in der GoodProxy or BadProxy -list!")
        print("alle Proxys wurden getestet!!!")

#        return HttpResponse(text, content_type="text/plain")
