from factura.admin import FacturaAdmin
from django.shortcuts import render
from django.http import HttpResponse
from .models import Factura, LineaFactura

# Create your views here.

def cliente(request):
    fc = Factura.objects.all()
    fac = LineaFactura.objects.all()
    return render(request, 'factura/pagina_principal.html', {
    'fc': fc,
    'fac':fac,
    })

