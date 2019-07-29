from django.shortcuts import render
from .models import Guia
# Create your views here.

def index(request):
    template_name = 'guias_index.html'
    context = {
        "Guias": Guia.objects.order_by("nome")
    }
    return render(request, template_name, context)