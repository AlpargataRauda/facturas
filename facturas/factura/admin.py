from django.contrib import admin
from .models import Factura, LineaFactura

class FacturaAdmin(admin.ModelAdmin):
    list_display=('id','numero', 'year', 'fecha', 'cliente_nombre')

admin.site.register(Factura, FacturaAdmin)

class LineaFacturaAdmin(admin.ModelAdmin):
    list_display =('nombre_producto', 'precio_unitario', 'unidades', 'iva')

admin.site.register(LineaFactura)
