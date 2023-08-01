from django.urls import path
from . import views

urlpatterns = [
    path('', views.Hello),
    path('Empresas/', views.Empresa),
    path('Cargo/', views.Cargos),
    path('Personal/', views.Personal)
]