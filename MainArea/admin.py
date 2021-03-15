from django.contrib import admin


from .models import Contact, ProxyContainer, UserProfileInfo
# Register your models here.


admin.site.register(Contact)
admin.site.register(ProxyContainer)
admin.site.register(UserProfileInfo)
