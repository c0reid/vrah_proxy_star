from django.contrib import admin
from .models import UserProxy, BadProxy, GoodProxy, LoadedPrxy
# Register your models here.


admin.site.register(UserProxy)
admin.site.register(BadProxy)
admin.site.register(GoodProxy)
admin.site.register(LoadedPrxy)
