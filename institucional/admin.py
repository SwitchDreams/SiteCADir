from django.contrib import admin
from .models import Postagem
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

@admin.register(Postagem)
class PostagemAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'