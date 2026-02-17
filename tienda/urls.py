from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('perfil/listar', views.listar_perfiles,name='listar_perfiles')
]
