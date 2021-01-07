from django.urls import path, include
from django.contrib import admin

from . import views

app_name = 'teretana'
urlpatterns = [

    path('',views.userPage, name = 'Home'),
    path('member', views.createMember , name = 'Member'),
    path('card' , views.createCard , name = 'Card'),

    path('update_member/<int:member_id>/', views.updateMember, name='UpdateM'),
    path('update_card/<int:card_id>/', views.updateCard, name='UpdateC'),

    path('deleteMember/<int:member_id>/', views.deleteMember, name='DeleteM'),
    path('deleteCard/<int:card_id>/', views.deleteCard, name='DeleteC')
]