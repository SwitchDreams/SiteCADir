from django.shortcuts import render
from .models import Programa
# Create your views here.

def index(request):
    template_name = 'programas_index.html'
    context = {
        "Programas" : Programa.objects.all()
    }
    return render(request, template_name, context)

def show(request, **kwargs):
    template_name = 'programas_show.html'
    context = {
        "Programa" : Programa.objects.filter(id=int(kwargs['pk'])).get()
    }
    return render(request, template_name, context)
