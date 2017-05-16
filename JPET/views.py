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

# dict_of_all_classes = {'scintype':ScinType, 
#                         'scin':Scin}

dict_of_all_form = {'scintype':ScinTypeForm,
                    'scin':ScinForm,
                    'setup':SetupForm,
                    'statustype':StatusTypeForm,
                    'status':StatusForm,
                    'frame':FrameForm,
                    'layer':LayerForm,
                    'slot':SlotForm,
                    'scininserted':ScinInsertetForm,
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
# def fieldsForModel(model_name):
#     modelFields = dict_of_all_classes[model_name]._meta.fields
#     newmodel = []
#     for i in modelFields:
#         newmodel.append(i.name)
#     return newmodel


def universal(request, model_name):
    try:
        #f =modelform_factory(dict_of_all_classes[model_name], fields=fieldsForModel(model_name=model_name))
        if request.method == "POST":
            print 'dffhghgfs'
            form = dict_of_all_form[model_name](request.POST)
            post = form.save()
            if form.is_valid():
                # post = form.save()
                print 'dffhs'
                post.save()
                return render(request, 'universal.html', {'form': form})
            else:
                print 'dffasshs'
                return render(request, 'universal.html', {'form': form})
        else:
            form = dict_of_all_form[model_name]()
            print 'dfs'
            return render(request, 'universal.html', {'form': form})
    except KeyError:
        return HttpResponseNotFound('<h1>Page not found</h1>')

