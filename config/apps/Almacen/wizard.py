import data_wizard
from apps.Almacen.models import *

data_wizard.register(Ordenes_Servicio)
data_wizard.register(Peticion_Impresiones_Color)
data_wizard.register(Solicitud_Equipo)
data_wizard.register(Prestamo_Eq_Pub)

