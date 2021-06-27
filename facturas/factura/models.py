from django.db import models
from django.contrib.auth.models import User
import datetime 
import time
from django.utils import timezone
from datetime import date


IVA_ACTUAL = 0.21


class Factura(models.Model):
    numero = models.IntegerField(default=0) 
    #Número de la factura
    fecha_emision = models.DateTimeField(auto_now_add= True)
    #Fecha
    cliente_nombre = models.CharField(max_length=50)
    #Nombre del cliente
    cliente_direccion = models.TextField(max_length=300)
    #Dirección del cliente

    def year(self):
        return self.fecha_emision.strftime('%Y')

    def fecha(self):
        return self.fecha_emision.strftime('%B/%d')

    def __str__(self) -> str:
        return self.cliente_nombre
    
    def lineas(self):
        return LineaFactura.objects.filter(propietario=self)

    def total(self):
        acumulador = 0
        for lin in self.lineas():
            acumulador += lin.precio_compra()
        return acumulador

    def iva(self):
        return self.total() * IVA_ACTUAL

    def total_mas_iva(self):
        return self.total() + self.iva()


class LineaFactura(models.Model):
    propietario = models.ForeignKey(
        Factura, 
        blank=False, 
        on_delete=models.PROTECT,
        null=True)
    nombre_producto = models.CharField(max_length=300)
        #Nombre del producto
    precio_unitario = models.FloatField(default=0)
    #Precio por unidad del producto
    unidades = models.IntegerField(default=1)
    #Total de unidades servidas
    iva = models.FloatField(default=1.21)

    def precio_compra(self):
        compra = (self.precio_unitario*self.unidades) 
        return compra

    def total_iva(self):
        return self.precio_compra() *(1+IVA_ACTUAL)

    def __str__(self) -> str:
        return self.nombre_producto