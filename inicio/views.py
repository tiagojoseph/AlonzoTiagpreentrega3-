from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from inicio.models import Propiedades

def propiedades (request):
    return HttpResponse ("propiedades")

def inicio (request):
    #return HttpResponse ("soy la pantalla de inicio")
    return render (request, "index.html")

def crear_propiedad (request):
    propiedad = Propiedades (metros_cuadrados = 300, ubicacion= "palermo", precio= "300.000 $")
    propiedad.save()
    return render (request, "crear_propiedad.html", {})