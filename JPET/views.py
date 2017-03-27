from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from django.forms import modelform_factory
from .models import *


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


D = {'scin/': Scin, 'scintype/': ScinType}
fieldsList = ['name','description', 'type', 'length', 'width', 'height ']

def universal(request, nazwa_modelu):
    try:
        if request.method == "POST":
            form = modelform_factory(model=D[nazwa_modelu], fields=[i for i in fieldsList if hasattr(D[nazwa_modelu], i)])
            if form.is_valid():
                post = form.save(commit=False)
                return redirect('index')
        else:
            form = modelform_factory(model=D[nazwa_modelu], fields=[i for i in fieldsList if hasattr(D[nazwa_modelu], i)])
        return render(request, 'universal.html', {'form': form})
    except KeyError:
        print nazwa_modelu
    # jak dac 404

