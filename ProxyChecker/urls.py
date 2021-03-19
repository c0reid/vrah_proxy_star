# pages/urls.py
from ProxyChecker import views
from django.urls import path,re_path
#from .views import ajax_view
app_name = 'ProxyChecker'




urlpatterns = [
    path("", views.ProxyChecker, name="PChecker"),
    re_path(r'upload/csv/$', views.upload_csv, name='upload_csv'),
    path('contact-form/', views.URL_String_Upload.as_view(), name='contact_form'),
    #path('save_url/', views.URL_String_Upload.as_view(), name='save_url'),
    path('ajax/', views.ajax_view, name="ajax"), # https://engineertodeveloper.com/how-to-use-ajax-with-django/
]
