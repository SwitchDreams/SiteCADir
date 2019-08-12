from django.contrib import admin
from .models import Postagem, TextoHistorico, PrestacaoDeContas, Atas, Logos, Estatuto
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
admin.site.register(PrestacaoDeContas)
admin.site.register(Atas)
admin.site.register(Logos)
admin.site.register(Estatuto)

@admin.register(Postagem)
class PostagemAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'

@admin.register(TextoHistorico)
class TextoHistoricoAdmin(SummernoteModelAdmin):
        summernote_fields = '__all__'
