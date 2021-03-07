

#import gevent
#from gevent import monkey
#monkey.patch_all()

#from getproxy import GetProxy
#g = GetProxy()

from proxy_checker import ProxyChecker
from ProxyChecker.models import UserProxy



def getDBProxys():
    dbProxys = UserProxy.objects.all().filter(user=1)
    testProxy = []
    for i in dbProxys:
        testProxy.append(i.ipAdress+":"+str(i.port))
        print(i.id, i.ipAdress+":"+str(i.port))
    #print(testProxy)
    print("Es sind:", len(dbProxys), "Datensätze")
    return testProxy

def checkPROXY_DB():
    dbProxys = UserProxy.objects.all().filter(user=1)
    #testProxy = []
    checker = ProxyChecker()
    for i in dbProxys:
        #testProxy.append(i.ipAdress+":"+str(i.port))
        print("Checke Proxy:", str(i.id), i.ipAdress+":"+str(i.port))
        tesstproxy=checker.check_proxy(i.ipAdress+":"+str(i.port))
        if tesstproxy == False:
                proxy = UserProxy.objects.get(id=i.id)
                proxy.delete()
                print("Delete Proxy by id:", i.id)


        print(tesstproxy)



"""
class ProxyChecker(object):
    def __init__(self, user,request):
        self.request = request
        self.user = user

    def GetDBProxysList(request, self):
        dbProxys = models.UserProxy.objects.filter(user=user)
        for i in range(100):

            print("Datenbankproxies abrufen!!")
            print(len(dbProxys))
            print(i)
        pass

            https://github.com/fate0/getproxy
            from getproxy import GetProxy
        g = GetProxy()

        # 1. 初始化，必须步骤
        g.init()

        # 2. 加载 input proxies 列表
        g.load_input_proxies()

        # 3. 验证 input proxies 列表
        g.validate_input_proxies()

        # 4. 加载 plugin
        g.load_plugins()

        # 5. 抓取 web proxies 列表
        g.grab_web_proxies()

        # 6. 验证 web proxies 列表
        g.validate_web_proxies()

        # 7. 保存当前所有已验证的 proxies 列表
        g.save_proxies()
"""
