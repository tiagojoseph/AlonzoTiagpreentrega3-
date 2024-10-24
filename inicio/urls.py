from django.urls import path 
from inicio.views import propiedades, inicio, crear_propiedad

urlpatterns = [
    path ("propiedad", propiedades),
    path ("", inicio),
    path ("creacion-propiedad/", crear_propiedad)
]