from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
#from django.forms import modelform_factory
from .models import *
from .forms import *
from django.http import HttpResponse, HttpResponseNotFound
from django.forms import Textarea 
# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render(request))


def runs(request):
    template = loader.get_template('runs.html')
    return HttpResponse(template.render(request))


def setups(request):
    template = loader.get_template('setups.html')
    return HttpResponse(template.render(request))


def faq(request):
    template = loader.get_template('faq.html')
    return HttpResponse(template.render(request))

def allModels(request):
    template = loader.get_template('allModels.html')
    return HttpResponse(template.render(request))

dict_of_all_form = {'scintype':ScinTypeForm,
                    'scin':ScinForm,
                    'setup':SetupForm,
                    'statustype':StatusTypeForm,
                    'status':StatusForm,
                    'frame':FrameForm,
                    'layer':LayerForm,
                    'slot':SlotForm,
                    'scininserted':ScinInsertedForm,
                    'pmmodel':PMModelForm,
                    'pm':PMForm,
                    'hv':HVForm,
                    'hvchannel':HVChannelForm,
                    'side':SideForm,
                    'pminserted':PMInsertedForm,
                    'run':RunForm,
                    'measurementtype':MeasurementTypeForm,
                    'measurement':MeasurementForm,
                    'radiationsourcetype':RadiationSourceTypeForm,
                    'radiationsource':RadiationSourceForm,
                    'radiationsourceinserted':RadiationSourceInsertedForm
                    }

def universal(request, model_name):
    try:
        if request.method == "POST":
            form = dict_of_all_form[model_name](request.POST)
            if form.is_valid():
                post = form.save()
                post.save()
                return redirect('allModels')
            else:
                return render(request, 'universal.html', {'form': form})
        else:
            form = dict_of_all_form[model_name]()
            return render(request, 'universal.html', {'form': form})
    except KeyError:
        return HttpResponseNotFound('<h1>Page not found</h1>')

