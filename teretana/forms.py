from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *


class MemberForm(ModelForm):
    class Meta:
        model = Member
        fields = '__all__'

class CardForm(ModelForm):
    class Meta:
        model = Card
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
