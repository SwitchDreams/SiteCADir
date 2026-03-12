# Site CADi UnB

Site institucional do Centro de Apoio ao Desenvolvimento Infantil da Universidade de Brasília (CADi UnB).

## Sobre o Projeto

Este é um site desenvolvido em Django que serves como portal de informações e comunicação do CADi UnB, oferecendo:

- **Programas**: Informações sobre os programas de desenvolvimento infantil oferecidos
- **Eventos**: Divulgação de eventos e atividades do centro
- **Guias**: Conteúdos educativos e orientações para famílias
- **Institucional**: Informações sobre o centro, histórico, estatuto e prestações de conta
- **Ouvidoria**: Canal para receber manifestações e feedback da comunidade

## Tecnologias

- Django 2.2.18
- Python 3
- SQLite
- django-summernote (editor de texto rico)
- django-bleach (sanitização de HTML)
- whitenoise (servidor de arquivos estáticos)

## Instalação

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Deploy

O site está disponível em: https://www.cadirunb.com.br
