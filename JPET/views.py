from django.shortcuts import render
from django.forms import inlineformset_factory
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
    InlineFormSet = inlineformset_factory(ScinType, Scin, form=ScinTypeForm)
    if request.method == "POST":
        form = ScinForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            return redirect('index')
    else:
        form = ScinForm()
    return render(request, 'scin.html', {'form': form})


def scinType(request):
    if request.method == "POST":
        form = ScinTypeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            return redirect('index')
    else:
        form = ScinTypeForm()
    return render(request, 'scinType.html', {'form': form})
