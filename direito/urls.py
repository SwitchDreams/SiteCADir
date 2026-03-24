from django.urls import path
from direito import views

app_name = 'direito'

urlpatterns = [
    path('', views.direito_brasileiro, name='direito_brasileiro'),
]
