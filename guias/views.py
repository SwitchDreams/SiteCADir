from django.shortcuts import render
from .models import Guia
# Create your views here.

def index(request):
    template_name = 'guias_index.html'
    context = {
        "Guias": Guia.objects.order_by("nome")
    }
    return render(request, template_name, context)

def assistencia_estudantil(request):
    template_name = 'assistencia_estudantil.html'
    context = {}
    return render(request, template_name, context)

def estrangeiro(request):
    template_name = 'estrangeiro.html'
    context = {}
    return render(request, template_name, context)

def fluxo(request):
    template_name = 'fluxo.html'
    context = {}
    return render(request, template_name, context)