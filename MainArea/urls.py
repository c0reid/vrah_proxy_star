# pages/urls.py
from django.urls import path , include, re_path
from MainArea import views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from django.conf import settings
from .views import contact_form , ContactFormView , validate_username, SignUpView



app_name = 'main'

urlpatterns = [
    path('dashboard/', views.home_page_view, name='home'),
    path("", views.UserDashboard, name="dashboard"),
    path('save_url/', views.UserDashboard, name='save_url'),
    path("register/", views.register, name="register"),
    path("logout", views.logout_request, name="logout"),
    path("login", views.login_request, name="login"),
    path('contact-form/', views.ContactFormView.as_view(), name='contact_form'),
    path("favicon.ico",RedirectView.as_view(url=staticfiles_storage.url("favicon.ico")),),
    # https://djangocentral.com/django-ajax-with-jquery/
    #########Making AJAX GET requests with Django and JQuery##########
    path('signup', SignUpView.as_view(), name='signup'),
    path('validate_username', validate_username, name='validate_username'),
    ###################
    ]


    #path("favicon.ico",RedirectView.as_view(url=staticfiles_storage.url("favicon.ico")),)
