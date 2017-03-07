from django import forms
from .models import Scin, ScinType
from django.contrib.auth.forms import AuthenticationForm

from django.forms.widgets import PasswordInput, TextInput


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'class': 'mdl-textfield__input', 'placeholder': 'Login'}))
    password = forms.CharField(widget=PasswordInput(attrs={'class': 'mdl-textfield__input', 'placeholder': 'Password'}))


class ScinForm(forms.ModelForm):
    class Meta:
        model = Scin
        fields = ('name', 'description', 'type', 'length', 'width', 'height',)


class ScinTypeForm(forms.ModelForm):
    class Meta:
        model = ScinType
        fields = ('name', 'description',)


