from django.shortcuts import render

def direito_brasileiro(request):
    template_name = 'direito/historico_direito_brasileiro.html'
    context = {}
    return render(request, template_name, context)
