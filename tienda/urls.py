from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('perfil/listar', views.listar_perfiles,name='listar_perfiles'),
    path('cesta/listar', views.listar_cestas,name='listar_cestas'),
    path('opinion/listar', views.listar_opiniones,name='listar_opiniones'),
    path('descuento/listar', views.listar_descuentos,name='listar_descuentos'),
]
