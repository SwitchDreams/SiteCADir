from django.shortcuts import render
from programas.models import Programa
# Create your views here.

def main_page(request):
    template_name  = 'main_page.html'
    context = {
        "Programas": Programa.objects.order_by('?')[:4]
    }
    return render(request, template_name, context)