from django import forms
from .models import Scin, ScinType, StatusType
from django.contrib.auth.forms import AuthenticationForm
from django.db import models
from django.forms.widgets import PasswordInput, TextInput
import collections


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'class': 'mdl-textfield__input', 'placeholder': 'Login'}))
    password = forms.CharField(widget=PasswordInput(attrs={'class': 'mdl-textfield__input', 'placeholder': 'Password'}))

#dict_of_all_classes = {'scin':Scin, 'scinType':ScinType}
#super(AnagraficaForm, self).__init__(*args, **kw)
#self.fields['nazione'] = forms.ChoiceField(choices = util.get_countries_tuple_list())
# class UniversalForm(forms.Form):
#     def __init__(self, *args, **kwargs):
#         class_name = kwargs.pop('model')
#         try:
#             self.class_object =  dict_of_all_classes[class_name]
#         except KeyError:
#             print("No %s in dict_of_all_classes"%cls)
#         super(UniversalForm, self).__init__(*args, **kwargs)
#         for i in listOfAllFields:
#             if hasattr(self.class_object, i):
#                 self.fields[i] = self.class_object.__getattribute__(i) 


