from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Factura(models.Model):
    numero: models.IntegerField(default=0) 
    #Número de la factura
    anio: models.DateField( auto_now=False, auto_now_add=False)
    #Año de la factura
    fecha_emision: models.DateField(auto_now=False, auto_now_add=False)
    #Fecha
    cliente_nombre: models.CharField(max_length=50)
    #Nombre del cliente
    cliente_direccion: models.TextField(max_length=300)
    #Dirección del cliente

    def __str__(self) -> str:
        return self.cliente_nombre

class LineaFactura(models.Model):
    nombre_producto: models.ForeignKey(
        Factura, 
        blank=False, 
        on_delete=models.PROTECT,)
        #Nombre del producto
    precio_unitario: models.FloatField(default=0)
    #Precio por unidad del producto
    unidades: models.IntegerField(default=1)
    #Total de unidades servidas

        

    def __str__(self) -> str:
        return self.nombre_producto