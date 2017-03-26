from django import forms
from .models import Scin, ScinType, StatusType
from django.contrib.auth.forms import AuthenticationForm
from django.db import models
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

listOfAllFields = ['name', 'description']
dict_of_all_classes = {'Scin':Scin, 'ScinType':ScinType}
#super(AnagraficaForm, self).__init__(*args, **kw)
#self.fields['nazione'] = forms.ChoiceField(choices = util.get_countries_tuple_list())
class UniversalForm(forms.Form):
    def __init__(self, *args, **kwargs):
        forms.__init__('class')
        for i in listOfAllFields:
            if hasattr(dict_of_all_classes['class'], i):
                self.fields[i] = dict_of_all_classes['class'].__getattribute__(i)  


