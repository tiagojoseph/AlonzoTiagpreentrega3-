from django.urls import path 
from inicio.views import propiedades, inicio, crear_propiedad

app_name = "inicio"

urlpatterns = [
    path ("propiedad", propiedades),
    path ("", inicio, name= "inicio" ),
    path ("crear-propiedad", crear_propiedad, name= "crear_propiedad")
]
    