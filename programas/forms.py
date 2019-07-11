from django import forms
from .models import Programa

class SelectPrograma(forms.Form):
    # Tipo Todos com uma append do Progama.TIPO_CHOICES
    # CHOICES1 = (('TOD', 'Todos')) + Programa.TIPOS_CHOICES
    CHOICES = (
        ('TOD', 'Todos'),
        ('ATL', 'Atlética'),
        ('EJ', 'Empresa Junior'),
        ('GE', 'Grupo de extensão'),
        ('OUT', 'Outros'),

    )
    field = forms.ChoiceField(label='' , widget=forms.Select(attrs={'class':'selectpicker btn-outline-dark'}), choices=CHOICES)