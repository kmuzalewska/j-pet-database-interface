from django import forms
from .models import *
from django.contrib.auth.forms import AuthenticationForm
from django.db import models
from django.forms.widgets import PasswordInput, TextInput
import collections
from django.forms import *

allWidget = {
    'name': TextInput(attrs={'class': 'mdl-textfield__input', 'placeholder': 'Name'}),
    'description': Textarea(attrs={'class': 'mdl-textfield__input', 'placeholder': 'Description'}),
    'length': NumberInput(attrs={'class': 'mdl-textfield__input', 'placeholder': 'Version', 'min': '0'}),
    'width': NumberInput(attrs={'class': 'mdl-textfield__input', 'placeholder': 'Version', 'min': '0'}),
    'height': NumberInput(attrs={'class': 'mdl-textfield__input', 'placeholder': 'Version', 'min': '0'}),
    'version': NumberInput(attrs={'class': 'mdl-textfield__input', 'placeholder': 'Version', 'min': '0'}),
    'createDate': DateTimeInput(attrs={'class': 'mdl-textfield__input', 'placeholder': 'Create date'}),
    'dateTime': DateTimeInput(attrs={'class': 'mdl-textfield__input', 'placeholder': 'Date time'}),
    'type': Select(attrs={'class': 'mdl-textfield__input'}),
    'generalStatus': Select(attrs={'class': 'mdl-textfield__input'}),
    'radius': NumberInput(attrs={'class': 'mdl-textfield__input', 'placeholder': 'Radius'}),
    'frame': Select(attrs={'class': 'mdl-textfield__input'}),
    'theta': NumberInput(attrs={'class': 'mdl-textfield__input', 'placeholder': 'Theta'}),
    'layer': Select(attrs={'class': 'mdl-textfield__input'}), 
    'parentSlot': Select(attrs={'class': 'mdl-textfield__input'}),
    'scin': Select(attrs={'class': 'mdl-textfield__input'}),
    'status': Select(attrs={'class': 'mdl-textfield__input'}),
    'slot': Select(attrs={'class': 'mdl-textfield__input'}),
    'setup':Select(attrs={'class': 'mdl-textfield__input'}),
    'attLength': NumberInput(attrs={'class': 'mdl-textfield__input', 'placeholder': 'Att Length'}),
    'velocity': NumberInput(attrs={'class': 'mdl-textfield__input', 'placeholder': 'Velocity'}),
    'zOffSet': NumberInput(attrs={'class': 'mdl-textfield__input', 'default':'0','placeholder': 'zOffSet'}),
    'producer': TextInput(attrs={'class': 'mdl-textfield__input', 'placeholder': 'Producer'}),
    'purchaseDate': DateTimeInput(attrs={'class': 'mdl-textfield__input', 'placeholder': 'Purchase Date'}),   
    'serialNumber': TextInput(attrs={'class': 'mdl-textfield__input', 'placeholder': 'Serial Number'}),
    'pmModel':Select(attrs={'class': 'mdl-textfield__input'}), 
    'maxHV': NumberInput(attrs={'class': 'mdl-textfield__input', 'placeholder': 'Max HV'}),
    'takesPositiveVoltage': CheckboxInput(attrs={'class': 'mdl-textfield__input'}),
    'driverPluginInfo': Textarea(attrs={'class': 'mdl-textfield__input', 'placeholder': 'Driver plugin info'}),
    'idX': TextInput(attrs={'class': 'mdl-textfield__input', 'placeholder': 'ID X'}),
    'maxV': NumberInput(attrs={'class': 'mdl-textfield__input', 'placeholder': 'Max V'}),
    'minV': NumberInput(attrs={'class': 'mdl-textfield__input', 'placeholder': 'Min V'}),
    'givesPositiveVoltage': CheckboxInput(attrs={'class': 'mdl-textfield__input'}),
    'hv': Select(attrs={'class': 'mdl-textfield__input'}),
    'side':Select(attrs={'class': 'mdl-textfield__input'}),
    'hvChannel':Select(attrs={'class': 'mdl-textfield__input'}),
    'pm':Select(attrs={'class': 'mdl-textfield__input'}),
    'fileName': TextInput(attrs={'class': 'mdl-textfield__input', 'placeholder': 'File name'}),
    'checksum': TextInput(attrs={'class': 'mdl-textfield__input', 'placeholder': 'Check sum'}),
    'run':Select(attrs={'class': 'mdl-textfield__input'}),
    'user':Select(attrs={'class': 'mdl-textfield__input'}),
    'startDateTime': DateTimeInput(attrs={'class': 'mdl-textfield__input', 'placeholder': 'Start Date Time'}),   
    'endDateTime': DateTimeInput(attrs={'class': 'mdl-textfield__input', 'placeholder': 'End Date Time'}),   
    'source':Select(attrs={'class': 'mdl-textfield__input'}),
    'measurement':Select(attrs={'class': 'mdl-textfield__input'}),
    'colimated': CheckboxInput(attrs={'class': 'mdl-textfield__input'}),
    'positionX': NumberInput(attrs={'class': 'mdl-textfield__input', 'placeholder': 'Position X'}),
    'positionY': NumberInput(attrs={'class': 'mdl-textfield__input', 'placeholder': 'Position Y'}),
    'positionZ': NumberInput(attrs={'class': 'mdl-textfield__input', 'placeholder': 'Position Z'}),


}
class LoginForm(AuthenticationForm):
    username = CharField(widget=TextInput(attrs={'class': 'mdl-textfield__input', 'placeholder': 'Login'}))
    password = CharField(widget=PasswordInput(attrs={'class': 'mdl-textfield__input', 'placeholder': 'Password'}))

class ScinTypeForm(ModelForm):

    class Meta:
        model = ScinType
        fields = '__all__'
        widgets = allWidget



class ScinForm(ModelForm):

    class Meta:
        model = Scin
        fields = '__all__'
        widgets = allWidget


class SetupForm(ModelForm):

    class Meta:
        model = Setup
        fields = '__all__'
        widgets = allWidget


class StatusTypeForm(ModelForm):

    class Meta:
        model = StatusType
        fields = '__all__'
        widgets = allWidget


class StatusForm(ModelForm):

    class Meta:
        model = Status
        fields = '__all__'
        widgets = allWidget


class FrameForm(ModelForm):

    class Meta:
        model = Frame
        fields = '__all__'
        widgets = allWidget


class LayerForm(ModelForm):

    class Meta:
        model = Layer
        fields = '__all__'
        widgets = allWidget


class SlotForm(ModelForm):

    class Meta:
        model = Slot
        fields = '__all__'
        widgets = allWidget


class ScinInsertedForm(ModelForm):

    class Meta:
        model = ScinInserted
        fields = '__all__'
        widgets = allWidget


class PMModelForm(ModelForm):

    class Meta:
        model = PMModel
        fields = '__all__'
        widgets = allWidget


class PMForm(ModelForm):

    class Meta:
        model = PM
        fields = '__all__'
        widgets = allWidget


class HVForm(ModelForm):

    class Meta:
        model = HV
        fields = '__all__'
        widgets = allWidget

class HVChannelForm(ModelForm):

    class Meta:
        model = HVChannel
        fields = '__all__'
        widgets = allWidget


class SideForm(ModelForm):

    class Meta:
        model = Side
        fields = '__all__'
        widgets = allWidget


class PMInsertedForm(ModelForm):

    class Meta:
        model = PMInserted
        fields = '__all__'
        widgets = allWidget


class RunForm(ModelForm):

    class Meta:
        model = Run
        fields = '__all__'
        widgets = allWidget


class MeasurementTypeForm(ModelForm):

    class Meta:
        model = MeasurementType
        fields = '__all__'
        widgets = allWidget


class MeasurementForm(ModelForm):

    class Meta:
        model = Measurement
        fields = '__all__'
        widgets = allWidget


class MeasurementForm(ModelForm):

    class Meta:
        model = Measurement
        fields = '__all__'
        widgets = allWidget


class RadiationSourceTypeForm(ModelForm):

    class Meta:
        model = RadiationSourceType
        fields = '__all__'
        widgets = allWidget


class RadiationSourceForm(ModelForm):

    class Meta:
        model = RadiationSource
        fields = '__all__'
        widgets = allWidget


class RadiationSourceInsertedForm(ModelForm):

    class Meta:
        model = RadiationSourceInserted
        fields = '__all__'
        widgets = allWidget
