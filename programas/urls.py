from django.urls import path, include
from programas import views

app_name = 'programas'

urlpatterns = [
    # Index Path
    path('', views.index, name='index'),
    # Show Path
    path('<int:pk>', views.show, name='show')
]