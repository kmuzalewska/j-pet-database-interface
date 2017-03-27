from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from django.forms import modelform_factory
from .models import *
from .forms import UniversalForm

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
        #if request.method == "POST":
        form = UniversalForm(request.POST, nazwa_modelu)
        print nazwa_modelu
        if form.is_valid():
            post = form.save(commit=False)
            return redirect('index')
        #else:
            #form = UniversalForm(nazwa_modelu)
        return render(request, 'universal.html', {'form': form})
    except KeyError:
        print nazwa_modelu
        print 'hello'
    # jak dac 404

