

#import gevent
#from gevent import monkey
#monkey.patch_all()

#from getproxy import GetProxy
#g = GetProxy()
from proxy_checker import ProxyChecker
from ProxyChecker.models import UserProxy, LoadedPrxy, GoodProxy, BadProxy
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Count, Max
from django.utils import timezone
from django.contrib.auth.models import User


#Colours
red="\033[1;31m"
green="\033[1;32m"
yellow="\033[1;33m"
blue="\033[1;34m"
defcol = "\033[0m"

def getDBProxys():
    dbProxys = UserProxy.objects.all().filter(user=1)
    testProxy = []
    for i in dbProxys:
        testProxy.append(i.ipAdress+":"+str(i.port))
        print(i.id, i.ipAdress+":"+str(i.port))
    #print(testProxy)
    print("Es sind:", len(dbProxys), "Datensätze")
    return testProxy

def LoadProxys():
    pass

def CleanUpMainProxyDatabase():
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

def checkPROXY_DB():
    CleanUpMainProxyDatabase()
    user = User.objects.get(id=1)
    dbProxys = UserProxy.objects.all().filter(user=user)
    badProxy = BadProxy.objects.all().filter(user=user)
    goodProxys = GoodProxy.objects.all().filter(user=user)
    #testProxy = []
    checker = ProxyChecker()
    for i in dbProxys:
        # ProxyId ran holen
        proxy = dbProxys.get(id=i.id)
        # ist der Proxy in der BadProxy List =
        badProxyCount=BadProxy.objects.filter(ipAdress=i.ipAdress,port=i.port).count()
        goodProxyCount=GoodProxy.objects.filter(ipAdress=i.ipAdress,port=i.port).count()
        if badProxyCount and goodProxyCount == 0:
            print(defcol+"Proxy not in Bad and Good -Proxylist\nChecking Proxy:", str(i.id), i.ipAdress+":"+str(i.port))
            tesstproxy=checker.check_proxy(i.ipAdress+":"+str(i.port))
            if tesstproxy == False:
                try:
                    newbadProxy = badProxy.create(user_id=1,
                                                    ipAdress=i.ipAdress,
                                                    port=i.port)
                    newbadProxy.save()
                    print(red+"Bad ProxyId:{}:added to BadProxys".format(i.id))

                    #Aktualsiere Badproxys
                    badProxy = BadProxy.objects.all().filter(user=user)
                except ObjectDoesNotExist as DoesNotExist:
                    print(red+"Fehler!!! ObjectDoesNotExist ")
            else:
                try:
                    if goodProxyCount == 0:
                        newgoodProxy = goodProxys.create(user_id=1,
                                                        ipAdress=i.ipAdress,
                                                        port=i.port,
                                                        protokol = tesstproxy['protocols'][0],
                                                        anonymitaetsLevel=tesstproxy["anonymity"],
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
