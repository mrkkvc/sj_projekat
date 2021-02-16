from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group

from .decorators import unauthentificated_user, allow_users, admin_only

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from teretana.models import Member,Card

from django.contrib.auth.decorators import login_required

def userPage(request):
    member = Member.objects.all()
    card = Card.objects.all()
    total_card = card.count()
    total_member = member.count()
    total_usingcard = Member.objects.filter(card_type = '3').count()
    return render(request, 'teretana/dashboard.html', {'member' : member, 'card' : card, 'total_card' : total_card, 'total_member' : total_member, 'total_usingcard' : total_usingcard})
