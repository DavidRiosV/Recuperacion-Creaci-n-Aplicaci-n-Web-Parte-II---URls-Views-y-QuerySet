from django.db import models

# Create your models here.

from django.db import models

# 1 Usuario/Cliente
class Usuario(models.Model):
    nombre = models.CharField(max_length=15)
    correo_electronico = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=20)
    fecha_registro = models.DateTimeField()

    def __str__(self):
        return self.nombre
    
# 2 Perfil del usuario/cliente
class Perfil_Usuario(models.Model):
    usuario=models.OneToOneField(Usuario, on_delete=models.CASCADE)

    nombre_usuario=models.CharField(max_length=15, unique=True)
    biografia=models.CharField(max_length=200)
    telefono=models.CharField(max_length=9)
    direccion=models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_usuario

# 3 Marca/Creador/Vendedor
class Marca (models.Model):
    nombre=models.CharField(max_length=20 ,unique=True)
    pais_origen=models.CharField(max_length=100, blank=True)
    descripcion=models.TextField(blank=True)
    año_fundacion=models.PositiveIntegerField(null=True,blank=True)

# 4 Descuento
class Descuento (models.Model):
    codigo=models.CharField(max_length=20 , unique=True)
    porcentaje=models.DecimalField(max_digits=5 , decimal_places=2)
    activo=models.BooleanField(default=True)
    fecha_expiracion=models.DateField()

# 5 Prenda de ropa
class Prenda (models.Model):
    marca=models.ForeignKey(Marca, on_delete=models.CASCADE)
    descuentos = models.ManyToManyField(Descuento, blank=True)

    TALLAS = [
        ('XS', 'XS'),
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
    ]
  
    nombre=models.CharField(max_length=100)
    descripcion=models.TextField(blank=True)
    precio=models.DecimalField(max_digits=8,decimal_places=2)
    talla=models.CharField(max_length=3, choices=TALLAS)

# 6 Cesta
class Cesta (models.Model):
    usuario=models.OneToOneField(Usuario, on_delete=models.CASCADE)
    prendas = models.ManyToManyField(Prenda)

    fecha_creacion=models.DateTimeField()
    activo=models.BooleanField()
    objetos_en_cesta=models.IntegerField()
    total=models.FloatField()

# 7 Inventario
class Inventario (models.Model):
    prenda=models.OneToOneField(Prenda, on_delete=models.CASCADE)

    cantidad_disponible=models.PositiveIntegerField(default=0)
    ubicacion_almacen=models.CharField(max_length=255,blank=True)
    stock_minimo=models.PositiveIntegerField(default=1)
    stock_maximo=models.PositiveIntegerField(default=100)

# 8 Pedido
class Pedido (models.Model):
    ESTADOS = [
        ('PEND', 'Pendiente'),
        ('PROC', 'Procesando'),
        ('ENV', 'Enviado'),
        ('ENT', 'Entregado'),
    ]
    
    usuario=models.ForeignKey(Usuario, on_delete=models.CASCADE)
    prendas = models.ManyToManyField(Prenda, through='Detalle_Pedido')

    fecha=models.DateTimeField(auto_now_add=True)
    total=models.DecimalField(max_digits=10,decimal_places=2,default=0)
    estado=models.CharField(max_length=4,choices=ESTADOS, default='PEND')
    direccion_envio = models.CharField(max_length=255)

# 9 Detalle_Pedido
class Detalle_Pedido (models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    prenda = models.ForeignKey(Prenda, on_delete=models.CASCADE)

    fecha_agregado = models.DateTimeField(auto_now_add=True)
    fecha_entrega = models.DateTimeField(null=True, blank=True)
    cantidad = models.PositiveIntegerField(default=1)
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

# 10 Opinion/Reseña
class Opinion (models.Model):
    usuario=models.ForeignKey(Usuario, on_delete=models.CASCADE)

    clasificacion=models.PositiveIntegerField()
    comentario=models.TextField(blank=True)
    fecha=models.DateField(auto_now_add=True)
    recomendado=models.BooleanField(default=True)