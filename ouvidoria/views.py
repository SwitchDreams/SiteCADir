from django.shortcuts import render
from .forms import FormsOuvidoria
from django.core.mail import send_mail
from .models import MensagemOuvidoria
import datetime


# Auxiliar functions
def categoria_clean(categoria):
    # Coletando o ano atual
    ano = datetime.datetime.now()
    ano = ano.year
    # Tratando o assunto e o text enviado
    start = datetime.date(ano, 1, 1)
    end = datetime.date(ano, 12, 31)
    assunto_enviado = str(categoria.nome) + "-" + str(
        MensagemOuvidoria.objects.filter(data__range=[start, end]).filter(categoria=categoria).count()) + "/" + str(ano)
    return assunto_enviado


def corpo_do_email(assunto, texto, email):
    corpo_do_texto = "Email Enviado da Ouvidoria do Site do CADir - Assunto: " + assunto + "\n"
    if email != "":
        corpo_do_texto += "O destinatário deseja resposta, envie para o e-mail: " + email + "\n"
    corpo_do_texto += texto
    return corpo_do_texto


# Create your views here.
def ouvidoria(request):
    template_name = 'ouvidoria.html'
    form = FormsOuvidoria(request.POST or None)
    context = {}
    if form.is_valid():
        # Escolher para onde enviar
        categoria = form.cleaned_data.get('categoria')
        # Assunto
        assunto = form.cleaned_data.get('assunto')
        # E-mail caso
        email = form.cleaned_data.get('email')
        # Texto
        texto = form.cleaned_data.get('texto')

        # Tratando dados da categoria
        assunto_enviado = categoria_clean(categoria)

        # Tratando dados do texto
        corpo_do_texto = corpo_do_email(assunto, texto, email)

        # Salvando dados na Model
        mensagem = MensagemOuvidoria(categoria=categoria)
        mensagem.save()

        # Email do cadir(Tem que ser uma lista)
        to_email = ["dreamsswitch@gmail.com"]

        # Enviando o e-mail
        send_mail(assunto_enviado, corpo_do_texto, "brad@sandboxd5f011b5c7d4421bb16957131f60fe01.mailgun.org", to_email, html_message=corpo_do_texto)
        context["thanks"] = "E-mail enviado com sucesso"
    context["form"] = form

    return render(request, template_name, context)
