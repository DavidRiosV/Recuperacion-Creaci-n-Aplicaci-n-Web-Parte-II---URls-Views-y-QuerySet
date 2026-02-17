from django.shortcuts import render
from tienda.models import Usuario,Perfil_Usuario,Marca,Descuento,Prenda,Inventario,Pedido,Opinion,Detalle_Pedido,Cesta
# Create your views here.

#Menu de inicio
def index(request):
    return render(request, 'tienda/index.html')

#Vista que muestra todos los perfiles de los usuarios

def listar_perfiles(request):
    perfiles = (Perfil_Usuario.objects.select_related("usuario").all())

    #SQL
    #perfiles = Perfil_Usuario.objects.raw("SELECT * FROM Tienda_Perfil_Usuario p" 
    #                                     +" JOIN Tienda_Usuario u ON u.id = p.usuario_id")

    return render(request, 'tienda/listar_perfiles.html', {'perfiles': perfiles})

