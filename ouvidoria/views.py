from django.shortcuts import render
from .forms import FormsOuvidoria
from django.core.mail import send_mail


# Create your views here.

def escolhe_email(tema):
    # Se tema 1
    if tema == "Tema1":
        return ['dreamsswitch@gmail.com']
    elif tema == "Tema2":
        return ['joaopedroassisdossantos@gmail.com']
    else:
        return ['pedro_a2312@hotmail.com']


def ouvidoria(request):
    template_name = 'ouvidoria.html'
    form = FormsOuvidoria(request.POST or None)
    context = {}
    if form.is_valid():
        # Escolher para onde enviar
        tema = form.cleaned_data.get('tema')
        # Assunto
        assunto = form.cleaned_data.get('assunto')
        # E-mail caso
        email = form.cleaned_data.get('email')
        # Texto
        texto = form.cleaned_data.get('texto')
        # Enviar email
        to_email = escolhe_email(tema)
        to_email = ['pedro_a2312@hotmail.com']
        send_mail(assunto, texto, "fromcadir@site.com", to_email)
        context["thanks"] = "E-mail enviado com sucesso"
    context["form"] = form
    return render(request, template_name, context)
