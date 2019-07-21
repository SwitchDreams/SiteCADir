from django.shortcuts import render
from .models import Programa
from .forms import SelectPrograma

# Create your views here.

def index(request):
    template_name = 'programas_index.html'
    form = SelectPrograma(request.POST or None)
    # Inicializa com todos os programas
    context = {"Programas": Programa.objects.all()}
    # Se o forms for válido
    if form.is_valid():
        # Coleta a opção
        answer = form.cleaned_data.get('field')
        # Mostra somente daquele tipo especifico
        if answer != "TOD":
            context["Programas"] = Programa.objects.filter(tipo=answer)
        # Mostra todos os programas
        else:
            context["Programas"] = Programa.objects.all()
    context["form"] = form
    return render(request, template_name, context)


def show(request, **kwargs):
    template_name = 'programas_show.html'
    context = {
        "Programa": Programa.objects.filter(id=int(kwargs['pk'])).get()
    }
    return render(request, template_name, context)
