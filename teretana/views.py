from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from . models import *

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