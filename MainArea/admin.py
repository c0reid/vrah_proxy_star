from django.contrib import admin


from .models import Contact, UserProfileInfo, UserProxys,City
# Register your models here.


admin.site.register(Contact)
admin.site.register(UserProfileInfo)
admin.site.register(UserProxys)
admin.site.register(City)
