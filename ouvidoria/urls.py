from django.urls import path, include
from ouvidoria import views

app_name = 'ouvidoria'

urlpatterns = [
    # Index Path
    path('', views.ouvidoria, name='ouvidoria'),
]