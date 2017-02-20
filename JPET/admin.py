from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Setup)
admin.site.register(Run)
admin.site.register(Status)
admin.site.register(StatusType)
admin.site.register(Frame)
admin.site.register(Layer)
admin.site.register(Slot)
admin.site.register(ScinType)
admin.site.register(Scin)
admin.site.register(ScinInserted)
# admin.site.register(ScintillatorCalibration)
admin.site.register(PMModel)
admin.site.register(PM)
admin.site.register(HV)
admin.site.register(HVChannel)
admin.site.register(Side)
admin.site.register(PMInserted)
# admin.site.register(PMCalibration)

