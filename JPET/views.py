from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from .forms import *
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


def scin(request):
    if request.method == "POST":
        form = ScinForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            return redirect('index')
    else:
        form = ScinForm()
    return render(request, 'universal.html', {'form': form})


def scinType(request):
    if request.method == "POST":
        form = ScinTypeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            return redirect('index')
    else:
        form = ScinTypeForm()
    return render(request, 'universal.html', {'form': form})


D = {'scin/': Scin, 'scintype/': ScinType}


def universal(request, nazwa_modelu):
    try:
        if request.method == "POST":
            form = UniversalForm(request.POST, model=D[nazwa_modelu])
            if form.is_valid():
                post = form.save(commit=False)
                return redirect('index')
        else:
            form = UniversalForm(request, model=D[nazwa_modelu])
        return render(request.GET, 'universal.html', {'form': form})
    except KeyError:
        print nazwa_modelu
    # jak dac 404