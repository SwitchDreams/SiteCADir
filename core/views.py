from django.shortcuts import render
from programas.models import Programa
from eventos.models import Evento
from guias.models import Guia
from .models import Fotos
# Create your views here.

def main_page(request):
    template_name  = 'main_page.html'
    context = {
        "Programas": Programa.objects.order_by('?')[:4],
        "Eventos": Evento.objects.order_by('start_day')[:3],
        "Guias": Guia.objects.order_by('?')[:4],
        "1Slider": Fotos.objects.filter(nome='1 Slider').get(),
        "2Slider": Fotos.objects.filter(nome='2 Slider').get(),
        "3Slider": Fotos.objects.filter(nome='3 Slider').get(),
        "1FotoDivisao": Fotos.objects.filter(nome='1 Foto Divisão').get(),
        "2FotoDivisao": Fotos.objects.filter(nome='2 Foto Divisão').get(),
    }
    return render(request, template_name, context)