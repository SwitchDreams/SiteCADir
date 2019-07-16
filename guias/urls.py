from django.urls import path, include
from guias import views

app_name = 'guias'

urlpatterns = [
    # Index Path
    path('', views.index, name='guias_index'),
]