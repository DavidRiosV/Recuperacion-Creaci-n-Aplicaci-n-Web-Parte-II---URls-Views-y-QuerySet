from django.urls import path,re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('perfil/listar', views.listar_perfiles,name='listar_perfiles'),
    path('cesta/listar', views.listar_cestas,name='listar_cestas'),
    path('opinion/listar', views.listar_opiniones,name='listar_opiniones'),
    path('inventario/listar/<int:cant>/<str:ubi>/', views.listar_inventarios, name='listar_inventarios'),
    path('descuentos/listar', views.listar_descuentos,name='listar_descuentos'),
    path('prendas/listar', views.listar_prendas,name='listar_prendas'),
    path('detalles_pedidos/listar', views.listar_detalles_pedidos,name='listar_detalles_pedidos'),
    path('usuarios/listar/<int:id>/', views.listar_usuarios,name='listar_usuarios'),
    path('marcas/listar/<str:nombre>/', views.listar_marcas,name='listar_marcas'),
    re_path(r'^pedidos/total/(?P<total>[0-9]+(\.[0-9]+)?)/$', views.listar_pedidos, name='listar_pedidos'),
]
