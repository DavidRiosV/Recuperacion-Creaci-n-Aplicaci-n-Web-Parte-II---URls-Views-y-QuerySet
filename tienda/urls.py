from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('usuarios/listar', views.listar_usuarios,name='listar_usuarios')
]
