from django import forms
from .models import Categoria
from django_summernote.widgets import SummernoteWidget

class FormsOuvidoria(forms.Form):
    # Campo acerca do tema
    categoria = forms.ModelChoiceField(label='Tema', widget=forms.Select(attrs={'class': 'form-control'}),
                                       queryset=Categoria.objects.all())
    # Campo acerca do e-mail
    email = forms.EmailField(label='E-mail', widget=forms.TextInput(attrs={'class': 'form-control'}),
                             help_text="Caso deseje resposta, preencha esse campo",
                             required=False
                             )
    # Campo acera do assunto
    assunto = forms.CharField(label='Assunto', widget=forms.TextInput(attrs={'class': 'form-control'}))
    # Campo acerta do texto ao ser enviado para o e-mail
    # texto = forms.CharField(label='Sua Mensagem', widget=forms.Textarea(attrs={'class': 'form-control'}))
    texto = forms.CharField(label='Sua Mensagem', widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}))