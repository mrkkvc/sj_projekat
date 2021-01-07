from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group

from .decorators import unauthentificated_user, allow_users, admin_only
from .forms import *

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

@unauthentificated_user
def registerPage(request):
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')

                group = Group.objects.get(name='customer')
                user.groups.add(group)

                messages.success(request, 'Account created for ' + username)

                return redirect('teretana:login')

        context = {'form':form}
        return render(request, 'teretana/register.html', context)

@unauthentificated_user
def loginPage(request):
        if request.method == 'POST':
           username = request.POST.get('username')
           password = request.POST.get('password')

           user = authenticate(request, username=username, password=password)

           if user is not None:
               login(request, user)
               return redirect('teretana:Home')
           else:
               messages.info(request, 'Username or Password is incorect')

        context = {}
        return render(request, 'teretana/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('teretana:login')

def userPage(request):
    member = Member.objects.all()
    card = Card.objects.all()
    return render(request, 'teretana/dashboard.html', {'member' : member, 'card' : card})

def createMember(request):
    form = MemberForm()
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            print(ValueError)

    context = {'form': form}

    return render(request, 'teretana/member.html', context)

def createCard(request):
    form = CardForm()
    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            print(ValueError)

    context = {'form': form}

    return render(request, 'teretana/card.html', context)

def updateMember(request, member_id):
    member = Member.objects.get(id = member_id)
    form = MemberForm(instance=member)
    if request.method == "POST":
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            print(ValueError)

    context = {'form':form}
    return render(request, 'teretana/member.html', context)

def updateCard(request, card_id):
    card = Card.objects.get(id = card_id)
    form = CardForm(instance=card)
    if request.method == "POST":
        form = CardForm(request.POST, instance=card)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            print(ValueError)

    context = {'form':form}
    return render(request, 'teretana/card.html', context)

def deleteMember(request, member_id):
    member = Member.objects.get(id=member_id)
    if request.method == "POST":
        member.delete()
        return redirect('/')

    context = {'item': member}
    return  render(request, 'teretana/delete_member.html', context)

def deleteCard(request, card_id):
    card = Card.objects.get(id=card_id)
    if request.method == "POST":
        card.delete()
        return redirect('/')

    context = {'item': card}
    return  render(request, 'teretana/delete_card.html', context)