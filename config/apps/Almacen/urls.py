from django.urls import include,path
from apps.Almacen.views import *




urlpatterns=[
    path('',HomeView, name="Index"),
    path('crearcuenta/', crear_cuenta.as_view(), name="CrearCuenta"),
    path('salir/', salir, name="salir"),
    path('acceder/',acceder,name="acceder"),
    path('sesion/',sesion,name="Sesion"),
    path('sesion/computadoras/', ComputadoraFormView.as_view(), name="computadora"),
    path('impresiones/',Peticion_Impresiones_ColorFormView.as_view(), name="Impresiones"),
        
    ]


