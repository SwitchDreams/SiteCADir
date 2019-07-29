from django.shortcuts import render
from .models import Postagem
# Create your views here.

def index(request):
    template_name = 'institucional_index.html'
    context = {
        "Postagens" : Postagem.objects.order_by('-created_at')
    }
    return render(request, template_name, context)

def postagem_show(request, **kwargs):
    template_name = 'postagem_show.html'
    context = {
        "Postagem": Postagem.objects.filter(nome=kwargs['pk']).get()
    }
    return render(request, template_name, context)