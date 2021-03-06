# pages/urls.py
from ProxyChecker import views
from django.urls import path,re_path

app_name = 'ProxyChecker'

urlpatterns = [
    path("", views.ProxyChecker, name="PChecker"),
    re_path(r'^upload/csv/$', views.upload_csv, name='upload_csv')
]
