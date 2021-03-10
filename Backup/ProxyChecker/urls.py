# pages/urls.py
from ProxyChecker import views
from django.urls import path,re_path
from ProxyChecker.src.checker import checkPROXY_DB

app_name = 'ProxyChecker'
# autostart = checkPROXY_DB()

urlpatterns = [
    path("", views.ProxyChecker, name="PChecker"),
    re_path(r'^upload/csv/$', views.upload_csv, name='upload_csv')
]
