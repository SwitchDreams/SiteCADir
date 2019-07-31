from django.shortcuts import render
from .models import Programa
from .forms import SelectPrograma
from google.cloud import texttospeech
import base64
# Create your views here.
def synthesize_text(text):
    """Synthesizes speech from the input string of text."""
    client = texttospeech.TextToSpeechClient()

    input_text = texttospeech.types.SynthesisInput(text=text)

    # Note: the voice can also be specified by name.
    # Names of voices can be retrieved with client.list_voices().
    voice = texttospeech.types.VoiceSelectionParams(
        language_code='en-US',
        ssml_gender=texttospeech.enums.SsmlVoiceGender.FEMALE)

    audio_config = texttospeech.types.AudioConfig(
        audio_encoding=texttospeech.enums.AudioEncoding.MP3)

    response = client.synthesize_speech(input_text, voice, audio_config)

    # The response's audio_content is binary.
    # Removing this because I do not care about writing the audio file
    # ----------------------------------------------------
    '''
    with open('output.mp3', 'wb') as out:
        out.write(response.audio_content)
        print('Audio content written to file "output.mp3"')
    '''
    # ----------------------------------------------------
    # instead return the encoded audio_content to decode and play in Javascript
    return base64.b64encode(response.audio_content).decode('ascii')



def index(request):
    template_name = 'programas_index.html'
    form = SelectPrograma(request.POST or None)
    # Inicializa com todos os programas
    context = {"Programas": Programa.objects.all()}
    # Se o forms for válido
    if form.is_valid():
        # Coleta a opção
        answer = form.cleaned_data.get('field')
        # Mostra somente daquele tipo especifico
        if answer != "TOD":
            context["Programas"] = Programa.objects.filter(tipo=answer)
        # Mostra todos os programas
        else:
            context["Programas"] = Programa.objects.all()
    context["form"] = form
    return render(request, template_name, context)


def show(request, **kwargs):
    template_name = 'programas_show.html'
    test_audio_content = synthesize_text('Test audio.')
    context = {
        "Audio": test_audio_content,
        "Programa": Programa.objects.filter(id=int(kwargs['pk'])).get()
    }
    return render(request, template_name, context)
