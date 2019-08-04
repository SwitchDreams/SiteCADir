from django.urls import path, include
from institucional import views

app_name = 'institucional'

urlpatterns = [
    # Index Path
    path('', views.index, name='institucional_index'),
    # Path Postagens
    path('postagens', views.postagens_index, name='postagens_index'),
    path('postagem/<str:pk>', views.postagem_show, name='postagem_show'),
    # Path Historico
    path('historico', views.historico, name='institucional_historico'),
    # Path Prestação de cotnas
    path('prestacao_conta', views.contas, name='institucional_contas'),
    # Path atas
    path('atas', views.atas, name='institucional_atas')
]