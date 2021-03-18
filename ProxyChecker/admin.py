from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(UserProxy)
admin.site.register(BadProxy)
admin.site.register(GoodProxy)
admin.site.register(ProxyStringUrl)
admin.site.register(Proxy)
admin.site.register(ProxyCheckStamp)
admin.site.register(ProxyLocation)
admin.site.register(BlackListed)
