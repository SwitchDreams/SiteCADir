from django.shortcuts import render
from .models import Evento


# Create your views here.

def index(request):
    template_name = 'eventos_index.html'
    context = {
        "Eventos": Evento.objects.all(),
    }
    return render(request, template_name, context)

def show(request, **kwargs):
    template_name = 'eventos_show.html'
    context = {
        "Evento": Evento.objects.filter(id=int(kwargs['pk'])).get()
    }
    return render(request, template_name, context)
