from django.shortcuts import render

# Create your views here.

def ouvidoria(request):
    template_name = 'ouvidoria.html'
    context = {}
    return render(request, template_name, context)