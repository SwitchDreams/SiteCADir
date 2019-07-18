from django.contrib import admin
from django.urls import path
from .models import Categoria, MensagemOuvidoria


# Register your models here.

@admin.register(Categoria)
class OuvidoriaAdmin(admin.ModelAdmin):
    change_list_template = "graph_ouvidoria.html"

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(request, extra_context=extra_context, )

        # response.context_data["dataGraph"] = [["Jorge", "1"], ["Malaquias", "2"], ["Tobias", "3"], ["Alfredo", "4"], ["Jose", "5"]]

        # Ariel exemplo pegando no periodo inteiro do site
        categorias = Categoria.objects.all()
        listaDataGraph = []
        for categoria in categorias:
            listaDataGraph.append([categoria.nome, MensagemOuvidoria.objects.filter(categoria=categoria).count()])
        response.context_data["dataGraph"] =listaDataGraph
        return response
