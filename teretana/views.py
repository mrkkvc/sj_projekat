from django.shortcuts import render
from django.http import HttpResponse

from . models import *

def userPage(request):
    member = Member.objects.all()
    card = Card.objects.all()
    return render(request, 'teretana/dashboard.html', {'member':member, 'card':card})
