from django.shortcuts import render

# Create your views here.

def main_page(request):
    template_name  = 'main_page.html'
    context = {}
    return render(request, template_name, context)