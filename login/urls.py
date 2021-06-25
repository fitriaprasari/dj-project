# from django.conf.urls import url,include
from django.urls import path,include
from django.contrib import admin

from . import views

urlpatterns = [
    path('login',views.login, name='login'),
    path('register',views.register, name='register')]