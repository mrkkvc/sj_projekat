from django.urls import path, include
from django.contrib import admin

from . import views

app_name = 'teretana'
urlpatterns = [

    path('',views.userPage, name = 'Home')
]