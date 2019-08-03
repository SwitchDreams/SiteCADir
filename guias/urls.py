from django.urls import path, include
from guias import views

app_name = 'guias'

urlpatterns = [
    # Index Path
    path('', views.index, name='guias_index'),
    path('assistencia_estudantil', views.assistencia_estudantil, name='assistencia_estudantil'),
    path('aluno_estrangeiro', views.estrangeiro, name='aluno_estrangeiro'),
    path('fluxo', views.fluxo, name='fluxo'),
]