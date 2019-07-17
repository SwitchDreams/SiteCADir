from django import forms


class FormsOuvidoria(forms.Form):
    # Temas da Ouvidoria
    CHOICES = (
        ('', ''),
        ('Tema1', 'Tema1'),
        ('Tema2', 'Tema2'),
        ('Tema3', 'Tema3'),
        ('Tema4', 'Tema4'),
        ('Tema5', 'Tema5'),

    )
    # Campo acerca do tema
    categoria = forms.ChoiceField(label='Tema', widget=forms.Select(attrs={'class': 'form-control'}), choices=CHOICES)
    # Campo acerca do e-mail
    email = forms.EmailField(label='E-mail', widget=forms.TextInput(attrs={'class': 'form-control'}),
                             help_text="Caso deseje resposta, preencha esse campo",
                             required=False
                             )
    # Campo acera do assunto
    assunto = forms.CharField(label='Assunto', widget=forms.TextInput(attrs={'class': 'form-control'}))
    # Campo acerta do texto ao ser enviado para o e-mail
    texto = forms.CharField(label='Sua Mensagem', widget=forms.Textarea(attrs={'class': 'form-control'}))
