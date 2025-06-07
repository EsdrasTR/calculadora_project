from django.urls import path
from . import views

app_name = 'metodos_numericos'
urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('calcular/', views.calcular_raiz, name='calcular'),
]