from django.shortcuts import render
from tienda.models import Usuario
# Create your views here.

#Menu de inicio
def index(request):
    return render(request, 'tienda/index.html')

#Vista que muestra todos los usuarios
def listar_usuarios(request):
    usuarios = (Usuario.objects.select_related('perfil_usuario', 'cesta').prefetch_related('pedido_set', 'opinion_set').all())
    return render(request, 'tienda/listar_usuarios.html', {'usuarios': usuarios})

