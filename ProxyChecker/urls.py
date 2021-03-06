# pages/urls.py
from django.urls import path
from ProxyChecker import views

app_name = 'ProxyChecker'

urlpatterns = [
    path("", views.ProxyChecker, name="PChecker"),
]
