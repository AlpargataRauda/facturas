from django.shortcuts import render
from django.http import HttpResponse
from .models import Factura, LineaFactura

# Create your views here.

def hola(request):
    return HttpResponse("Hola, Mundo")

def cliente(request, id):
    fc = Factura.objects.get()
    lf = LineaFactura.objects.get()
    return render(request, 'factura/pagina_principal.html', {
    'fc': fc,
    'lf': lf,
    })