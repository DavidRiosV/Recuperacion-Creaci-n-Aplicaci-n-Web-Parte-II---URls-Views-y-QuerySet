from django.core.management.base import BaseCommand
from faker import Faker
from tienda.models import *
from django.utils import timezone
import random




class Command(BaseCommand):
   help = 'Genera datos falsos para toda la base de datos'


   def handle(self, *args, **options):
       fake = Faker()


       # =====================
       # CREAR MARCAS
       # =====================
       marcas = []
       for _ in range(5):
           marca = Marca.objects.create(
               nombre=fake.unique.company(),
               pais_origen=fake.country(),
               descripcion=fake.text(max_nb_chars=100),
               año_fundacion=random.randint(1990, 2023)
           )
           marcas.append(marca)


       # =====================
       # CREAR DESCUENTOS
       # =====================
       descuentos = []
       for _ in range(5):
           descuento = Descuento.objects.create(
               codigo=fake.unique.bothify(text='DESC###'),
               porcentaje=random.randint(5, 50),
               activo=True,
               fecha_expiracion=fake.future_date()
           )
           descuentos.append(descuento)


       # =====================
       # CREAR PRENDAS
       # =====================
       prendas = []
       tallas = ['XS', 'S', 'M', 'L', 'XL']


       for _ in range(20):
           prenda = Prenda.objects.create(
               marca=random.choice(marcas),
               nombre=fake.word().capitalize(),
               descripcion=fake.text(max_nb_chars=150),
               precio=round(random.uniform(10, 150), 2),
               talla=random.choice(tallas)
           )


           # Añadir descuentos aleatorios
           prenda.descuentos.set(random.sample(descuentos, random.randint(0, 2)))


           prendas.append(prenda)


           # Crear inventario para cada prenda
           Inventario.objects.create(
               prenda=prenda,
               cantidad_disponible=random.randint(0, 100),
               ubicacion_almacen=fake.city(),
               stock_minimo=5,
               stock_maximo=200
           )


       # =====================
       # CREAR USUARIOS + PERFIL + CESTA
       # =====================
       usuarios = []


       for _ in range(10):
           usuario = Usuario.objects.create(
               nombre=fake.first_name(),
               correo_electronico=fake.unique.email(),
               contraseña=fake.password(length=10),
               fecha_registro=timezone.now()
           )


           Perfil_Usuario.objects.create(
               usuario=usuario,
               nombre_usuario=fake.unique.user_name(),
               biografia=fake.text(max_nb_chars=100),
               telefono=fake.msisdn()[:9],
               direccion=fake.address()
           )


           cesta = Cesta.objects.create(
               usuario=usuario,
               fecha_creacion=timezone.now(),
               activo=True,
               objetos_en_cesta=0,
               total=0
           )


           # Añadir prendas aleatorias a la cesta
           prendas_cesta = random.sample(prendas, random.randint(1, 5))
           cesta.prendas.set(prendas_cesta)
           cesta.objetos_en_cesta = len(prendas_cesta)
           cesta.total = sum([p.precio for p in prendas_cesta])
           cesta.save()


           usuarios.append(usuario)


       # =====================
       # CREAR PEDIDOS + DETALLE_PEDIDO
       # =====================
       for usuario in usuarios:
           for _ in range(random.randint(1, 3)):
               pedido = Pedido.objects.create(
                   usuario=usuario,
                   fecha=timezone.now(),
                   total=0,
                   estado=random.choice(['PEND', 'PROC', 'ENV', 'ENT']),
                   direccion_envio=fake.address()
               )


               prendas_pedido = random.sample(prendas, random.randint(1, 4))


               total_pedido = 0


               for prenda in prendas_pedido:
                   cantidad = random.randint(1, 3)
                   precio = prenda.precio
                   total_pedido += precio * cantidad


                   Detalle_Pedido.objects.create(
                       pedido=pedido,
                       prenda=prenda,
                       cantidad=cantidad,
                       precio=precio,
                       fecha_entrega=None
                   )


               pedido.total = total_pedido
               pedido.save()


       # =====================
       # CREAR OPINIONES
       # =====================
       for _ in range(20):
           Opinion.objects.create(
               usuario=random.choice(usuarios),
               clasificacion=random.randint(1, 5),
               comentario=fake.text(max_nb_chars=150),
               recomendado=random.choice([True, False])
           )


       self.stdout.write(self.style.SUCCESS('Base de datos rellenada correctamente 🔥'))