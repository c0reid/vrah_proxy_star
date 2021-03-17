from django.contrib import admin
from .models import UserProxy, BadProxy, GoodProxy, LoadedPrxy,ProxyStringUrl, Proxy ,BadProxyy, GoodProxyy
# Register your models here.


admin.site.register(UserProxy)
admin.site.register(BadProxy)
admin.site.register(GoodProxy)
admin.site.register(LoadedPrxy)
admin.site.register(ProxyStringUrl)
admin.site.register(Proxy)
admin.site.register(BadProxyy)
admin.site.register(GoodProxyy)
