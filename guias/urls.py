from django.urls import path, include
from guias import views

app_name = 'guias'

urlpatterns = [
    # Index Path
    path('', views.index, name='guias_index'),
    path('assistencia_estudantil', views.assistencia_estudantil, name='assistencia_estudantil'),
    path('aluno_estrangeiro', views.estrangeiro, name='aluno_estrangeiro'),
    path('fluxo', views.fluxo, name='fluxo'),
    path('manual_do_calouro', views.calouro, name='manual_do_calouro'),
    path('matricula_web', views.matricula_web, name='matricula_web'),
    path('monitoria', views.monitoria, name='monitoria')
]