from django.contrib import admin
from .models import Postagem, TextoHistorico, PrestacaoDeContas
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
admin.site.register(PrestacaoDeContas)

@admin.register(Postagem)
class PostagemAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'

@admin.register(TextoHistorico)
class TextoHistoricoAdmin(SummernoteModelAdmin):
        summernote_fields = '__all__'
