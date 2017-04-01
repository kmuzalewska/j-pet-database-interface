from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from django.forms import modelform_factory
from .models import *
#from .forms import UniversalForm
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

dict_of_all_classes = {'scintype':(ScinType, ("name", "description")), 'scin':(Scin, ('name', 'description', 'type', 'length', 'width', 'height',))}

def universal(request, nazwa_modelu):
    try:#if request.method == "POST":
        f =modelform_factory(dict_of_all_classes[nazwa_modelu][0], fields=dict_of_all_classes[nazwa_modelu][1])                #       UniversalForm(request.POST, model=nazwa_modelu) 
        print 'he'
        form = f()
        print nazwa_modelu
        if form.is_valid():
            #print(form.fields)
            post = form.save()
            return redirect('index')
        #else:
            #form = UniversalForm(nazwa_modelu)
        return render(request, 'universal.html', {'form': form})
    except KeyError:
        #print nazwa_modelu
        print 'hello'
    # jak dac 404

