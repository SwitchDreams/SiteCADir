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

def calouro(request):
    template_name = 'manual_do_calouro.html'
    context = {}
    return render(request, template_name, context)

def matricula_web(request):
    template_name = 'matricula_web.html'
    context = {}
    return render(request, template_name, context)

def monitoria(request):
    template_name = 'monitoria.html'
    context = {}
    return render(request, template_name, context)

def pcne(request):
    template_name = 'pcne.html'
    context = {}
    return render(request, template_name, context)

def predios(request):
    template_name = 'predios_unb.html'
    context = {}
    return render(request, template_name, context)

def tranferencia(request):
    template_name = 'transferencia.html'
    context = {}
    return render(request, template_name, context)

def transporte(request):
    template_name = 'transporte.html'
    context = {}
    return render(request, template_name, context)