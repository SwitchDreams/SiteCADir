from django.urls import path, include
from institucional import views

app_name = 'institucional'

urlpatterns = [
    # Index Path
    path('', views.index, name='institucional_index'),
]