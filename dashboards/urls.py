from django.urls import path, re_path
from django.conf.urls import url
from . import views

app_name = 'dashboards'

urlpatterns = [
    # user dashboards
    path('user_dashboard/', views.user_dashboard, name="user_dashboard"),
    ]