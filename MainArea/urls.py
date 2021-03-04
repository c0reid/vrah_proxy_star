# pages/urls.py
from django.urls import path
from MainArea import views

app_name = 'main'

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path("register/", views.register, name="register"),
    path("logout", views.logout_request, name="logout"),
    path("login", views.login_request, name="login"),

]
