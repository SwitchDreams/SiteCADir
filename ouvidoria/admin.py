from django.contrib import admin
from django.urls import path
from .models import Categoria


# Register your models here.

@admin.register(Categoria)
class OuvidoriaAdmin(admin.ModelAdmin):
    change_list_template = "graph_ouvidoria.html"

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(request, extra_context=extra_context, )

        response.context_data["dataGraph"] = [["Jorge", "1"], ["Malaquias", "2"], ["Tobias", "3"], ["Alfredo", "4"],
                                              ["Jose", "5"]]
        return response
