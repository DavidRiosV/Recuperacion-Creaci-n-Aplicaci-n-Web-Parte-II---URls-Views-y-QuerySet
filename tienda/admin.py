from django.contrib import admin

# Register your models here.

from .models import Usuario,Perfil_Usuario,Marca,Descuento,Prenda,Cesta,Inventario,Pedido,Detalle_Pedido,Opinion

admin.site.register(Usuario)
admin.site.register(Perfil_Usuario)
admin.site.register(Marca)
admin.site.register(Descuento)
admin.site.register(Prenda)
admin.site.register(Cesta)
admin.site.register(Inventario)
admin.site.register(Pedido)
admin.site.register(Detalle_Pedido)
admin.site.register(Opinion)