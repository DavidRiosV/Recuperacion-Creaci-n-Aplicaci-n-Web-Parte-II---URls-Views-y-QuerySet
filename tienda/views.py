from django.shortcuts import render
from tienda.models import Usuario,Perfil_Usuario,Marca,Descuento,Prenda,Inventario,Pedido,Opinion,Detalle_Pedido,Cesta
from django.db.models import Q

#Menu de inicio
def index(request):
    return render(request, 'tienda/index.html')

#Vista que muestra todos los perfiles de los usuarios

def listar_perfiles(request):
    perfiles = (Perfil_Usuario.objects.select_related("usuario").all())

    #SQL
    #perfiles = Perfil_Usuario.objects.raw("SELECT * FROM Tienda_Perfil_Usuario p" 
    #                                   +" JOIN Tienda_Usuario u ON u.id = p.usuario_id")

    return render(request, 'tienda/listar_perfiles.html', {'perfiles': perfiles})

#Vista que muestra todas las cestas ordenadas por objetos_en_cesta

def listar_cestas(request):
    cestas = (Cesta.objects.select_related("usuario").prefetch_related("prendas")).order_by("objetos_en_cesta")

    #SQL
    #cestas = Cesta.objects.raw("""
    #   SELECT *
    #   FROM Tienda_Cesta c
    #   JOIN Tienda_Usuario u ON u.id = c.usuario_id
    #   ORDER BY c.objetos_en_cesta
    #""")

    return render(request, 'tienda/listar_cestas.html', {'cestas': cestas})

#Vista que muestra todas las opiniones cuya valoracion sea 5 y lo recomiendan.

def listar_opiniones (request):
    opiniones = Opinion.objects.select_related("usuario")
    opiniones = opiniones.filter(clasificacion=5, recomendado=True)

    #SQL
    #opiniones = Opinion.objects.raw("""
    #   SELECT *
    #   FROM Tienda_Opinion o
    #   JOIN Tienda_Usuario u ON u.id = o.usuario_id
    #   WHERE o.clasificacion=5 AND o.recomendado=TRUE
    #""")

    return render(request, 'tienda/listar_opiniones.html', {'opiniones': opiniones})

#Vista que se le pase un entero que sera el porcentaje y debe de cumplir que solo muestre los que tengan ese % o la ubicacion es la pasada.

def listar_inventarios (request,cant,ubi):
    inventarios = Inventario.objects.select_related("prenda").filter(Q(cantidad_disponible=cant)|Q(ubicacion_almacen=ubi))

    #SQL
    #inventarios = Inventario.objects.raw("""
    #    SELECT i.*
    #    FROM Tienda_Inventario i
    #    JOIN Tienda_Prenda p ON p.id = i.prenda_id
    #    WHERE i.cantidad_disponible = %s OR i.ubicacion_almacen = %s
    #""", [cant, ubi])

    return render(request, 'tienda/listar_inventarios.html', {'inventarios': inventarios})

#Vista que ordena los descuentos por porcentaje y muestra el que mayor porcentaje tiene.

def listar_descuentos(request):
    descuentos = Descuento.objects.prefetch_related("prenda_set").order_by("-porcentaje")[:1]

    # SQL
    #descuentos = Descuento.objects.raw("""
    #   SELECT *
    #   FROM Tienda_Descuento d
    #   JOIN Tienda_Prenda_descuentos pd ON pd.descuento_id = d.id
    #   JOIN Tienda_Prenda p ON p.id = pd.prenda_id
    #   ORDER BY d.porcentaje DESC
    #   LIMIT 1;
    #""")
    return render(request, 'tienda/listar_descuentos.html', {'descuentos': descuentos})

#Vista que muestra las prendas que no tienen descuentos.

def listar_prendas(request):
   prendas = Prenda.objects.select_related("marca","inventario").prefetch_related("descuentos","cesta_set","pedido_set","detalle_pedido_set").filter(descuentos__isnull=True)

   #SQL
   #Necesito ayuda de Jorge
  
   return render(request, 'tienda/listar_prendas.html', {'prendas': prendas})