from django.urls import path, include
from eventos import views

app_name = 'eventos'

urlpatterns = [
    # Index Path
    path('', views.index, name='eventos_index'),
    #show Path
    path('<int:pk>', views.show, name='show')
]