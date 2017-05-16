from django import forms
from .models import Scin, ScinType, StatusType
from django.contrib.auth.forms import AuthenticationForm
from django.db import models
from django.forms.widgets import PasswordInput, TextInput
import collections


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'class': 'mdl-textfield__input', 'placeholder': 'Login'}))
    password = forms.CharField(widget=PasswordInput(attrs={'class': 'mdl-textfield__input', 'placeholder': 'Password'}))


# dict_of_all_classes = {'scintype':ScinType, 
#                         'scin':Scin}


# class UniversalForm(forms.Form):
#     def __init__(self, model_name):
#         super(UniversalForm, self).__init__(*args, **kwargs)
#         self.model_name = model_name
#         self.f = dict_of_all_classes[self.model_name]
#         name = self.f.__name__.lower()
#         setattr(self, name, self.f(*args, **kwargs))
#         form = getattr(self, name)
#         self.fields.update(form.fields)
#         self.initial.update(form.initial)

#     def fieldsForModel(self, model_name):
#         self.modelFields = dict_of_all_classes[model_name]._meta.fields
#         newmodel = []
#         for i in modelFields:
#             newmodel.append(i.name)
#         return newmodel

class ScinTypeForm(forms.ModelForm):

    class Meta:
        model = ScinType
        fields = '__all__'


class ScinForm(forms.ModelForm):

    class Meta:
        model = Scin
        fields = '__all__'


class SetupForm(forms.ModelForm):

    class Meta:
        model = Setup
        fields = '__all__'


class StatusTypeForm(forms.ModelForm):

    class Meta:
        model = StatusType
        fields = '__all__'


class StatusForm(forms.ModelForm):

    class Meta:
        model = Status
        fields = '__all__'


class FrameForm(forms.ModelForm):

    class Meta:
        model = Frame
        fields = '__all__'


class LayerForm(forms.ModelForm):

    class Meta:
        model = Layer
        fields = '__all__'


class SlotForm(forms.ModelForm):

    class Meta:
        model = Slot
        fields = '__all__'


class ScinInsertetForm(forms.ModelForm):

    class Meta:
        model = ScinInsertet
        fields = '__all__'


class PMModelForm(forms.ModelForm):

    class Meta:
        model = PMModel
        fields = '__all__'


class PMForm(forms.ModelForm):

    class Meta:
        model = PM
        fields = '__all__'


class HVForm(forms.ModelForm):

    class Meta:
        model = HV
        fields = '__all__'

class HVChannelForm(forms.ModelForm):

    class Meta:
        model = HVChannel
        fields = '__all__'


class SideForm(forms.ModelForm):

    class Meta:
        model = Side
        fields = '__all__'


class PMInsertedForm(forms.ModelForm):

    class Meta:
        model = PMInserted
        fields = '__all__'


class RunForm(forms.ModelForm):

    class Meta:
        model = Run
        fields = '__all__'


class MeasurementTypeForm(forms.ModelForm):

    class Meta:
        model = MeasurementType
        fields = '__all__'


class MeasurementForm(forms.ModelForm):

    class Meta:
        model = Measurement
        fields = '__all__'


class MeasurementForm(forms.ModelForm):

    class Meta:
        model = Measurement
        fields = '__all__'


class RadiationSourceTypeForm(forms.ModelForm):

    class Meta:
        model = RadiationSourceType
        fields = '__all__'


class RadiationSourceForm(forms.ModelForm):

    class Meta:
        model = RadiationSource
        fields = '__all__'


class RadiationSourceInsertedForm(forms.ModelForm):

    class Meta:
        model = RadiationSourceInserted
        fields = '__all__'