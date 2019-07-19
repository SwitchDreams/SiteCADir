from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Programa
# Register your models here.

@admin.register(Programa)
class ProgramaAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'