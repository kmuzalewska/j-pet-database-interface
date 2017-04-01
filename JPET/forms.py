from django import forms
from .models import Scin, ScinType, StatusType
from django.contrib.auth.forms import AuthenticationForm
from django.db import models
from django.forms.widgets import PasswordInput, TextInput
import collections


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'class': 'mdl-textfield__input', 'placeholder': 'Login'}))
    password = forms.CharField(widget=PasswordInput(attrs={'class': 'mdl-textfield__input', 'placeholder': 'Password'}))


