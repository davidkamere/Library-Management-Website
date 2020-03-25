from django.urls import path, re_path
from django.conf.urls import url
from . import views
from django.contrib.auth.views import LoginView

app_name = 'users'
urlpatterns = [
    # Log in Page
    path('register/', views.register, name="register"),
    ]
