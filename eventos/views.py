from django.shortcuts import render
from .models import Evento


# Create your views here.

def index(request):
    template_name = 'eventos_index.html'
    context = {
        "Eventos": Evento.objects.all(),
    }
    return render(request, template_name, context)
