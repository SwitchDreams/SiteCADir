from django.shortcuts import render
from .models import Postagem
from datetime import datetime
from django.utils import timezone
from django.core.paginator import Paginator


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
    postagem_list = Postagem.objects.order_by('-created_at')
    paginator = Paginator(postagem_list, 10)

    page = request.GET.get('page')
    postagens = paginator.get_page(page)
    context = {
        "Postagens": postagens,
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
