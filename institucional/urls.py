from django.urls import path, include
from institucional import views

app_name = 'institucional'

urlpatterns = [
    # Index Path
    path('', views.index, name='institucional_index'),
    # Show Path
    path('postagem/<str:pk>', views.postagem_show, name='postagem_show')
]