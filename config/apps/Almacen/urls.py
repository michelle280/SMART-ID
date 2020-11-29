from django.urls import path
from apps.Almacen.views import *


urlpatterns=[
    path('', index, name="Index"),
    path('login/', login.as_view(),name="login"),
    path('salir/', salir, name="salir"),
    path('acceder/',acceder,name="acceder"),
    ]


