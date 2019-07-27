import datetime
from email.mime.image import MIMEImage

import bs4
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render
from django.template.loader import render_to_string

from .forms import FormsOuvidoria
from .models import MensagemOuvidoria


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

def image_finder(tag):
    return (tag.name == u'img' or
            tag.name == u'table' and tag.has_key('background'))

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

        html_content = render_to_string('template_email.html', {'conteudo': corpo_do_texto})

        # Processando as imagens do e-mail
        soup = bs4.BeautifulSoup(html_content)
        images = []
        added_images = []
        for index, tag in enumerate(soup.findAll(image_finder)):
            if tag.name == u'img':
                name = 'src'
            elif tag.name == u'table':
                name = 'background'
            # If the image was already added, skip it.
            if tag[name] in added_images:
                continue
            added_images.append(tag[name])
            images.append((tag[name], 'img%d' % index))
            tag[name] = 'cid:img%d' % index
        html_content = str(soup)

        # Testando novo formato de envio
        email = EmailMultiAlternatives(
            subject=assunto_enviado,
            body=html_content,
            from_email="brad@sandboxd5f011b5c7d4421bb16957131f60fe01.mailgun.org",
            to=to_email
        )

        # Adicionando as img no e-mail
        for filename, file_id in images:
            image_file = open(settings.BASE_DIR + filename, 'rb')
            msg_image = MIMEImage(image_file.read())
            image_file.close()
            msg_image.add_header('Content-ID', '<%s>' % file_id)
            email.attach(msg_image)

        email.content_subtype = "html"

        # Enviando o e-mail
        email.send()
        context["thanks"] = "E-mail enviado com sucesso"

    context["form"] = form

    return render(request, template_name, context)
