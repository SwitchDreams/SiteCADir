from django.shortcuts import render
from .forms import FormsOuvidoria
from django.core.mail import send_mail
from .models import MensagemOuvidoria
import datetime


# Auxiliar functions
def categoria_clean(categoria):
    # Coletando o ano atual
    ano = datetime.datetime.year
    # Tratando o assunto e o text enviado
    start = datetime.date(int(ano), 1, 1)
    end = datetime.date(int(ano), 12, 31)
    assunto_enviado = categoria + MensagemOuvidoria.objects.filter(data__range=[start, end]).count + ano
    print(assunto_enviado)
    return assunto_enviado


def corpo_do_email(assunto, texto, email):
    corpo_do_texto = "Email Enviado da Ouvidoaria do Site do CADir - Assunto: " + assunto + "/n"
    if email != None:
        corpo_do_texto += "O destinatário deseja resposta, envie para o e-mail: " + email + "/n"
    else:
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

        # Email do cadir
        to_email = "cadirunb@unb.com.br"

        # Enviando o e-mail
        send_mail(assunto_enviado, corpo_do_texto, "brad@sandboxd5f011b5c7d4421bb16957131f60fe01.mailgun.org", to_email)
        context["thanks"] = "E-mail enviado com sucesso"
    context["form"] = form

    return render(request, template_name, context)
