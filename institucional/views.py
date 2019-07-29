from django.shortcuts import render
from .models import Postagem
from datetime import datetime
from django.utils import timezone


# Create your views here.

def index(request):
    template_name = 'institucional_index.html'
    context = {
        "Postagens": Postagem.objects.order_by('-created_at')[:5],
        "Hoje": timezone.now()
    }
    return render(request, template_name, context)


def postagens_index(request):
    template_name = 'postagens_index.html'
    context = {
        "Postagens": Postagem.objects.order_by('-created_at'),
        "Hoje": timezone.now()
    }
    return render(request, template_name, context)


def postagem_show(request, **kwargs):
    template_name = 'postagem_show.html'
    context = {
        "Postagem": Postagem.objects.filter(nome=kwargs['pk']).get(),
        "Hoje": timezone.now()
    }
    return render(request, template_name, context)
