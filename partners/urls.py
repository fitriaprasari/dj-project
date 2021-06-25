# from django.conf.urls import url,include
from django.urls import path,include
from django.contrib import admin

from . import views

urlpatterns = [
    path('partners',views.partners, name='partners'),
    path('details',views.detail, name='details'),]