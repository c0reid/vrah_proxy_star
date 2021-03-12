# pages/urls.py
from django.urls import path , include
from MainArea import views
#from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from django.conf import settings


app_name = 'main'

urlpatterns = [
    path('dashboard/', views.home_page_view, name='home'),
    path("", views.UserDashboard, name="dashboard"),
    path("register/", views.register, name="register"),
    path("logout", views.logout_request, name="logout"),
    path("login", views.login_request, name="login"),
]


#    path("favicon.ico",RedirectView.as_view(url=staticfiles_storage.url("favicon.ico")),)
