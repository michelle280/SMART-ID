from import_export import resources
from apps.Almacen.models import *


class EmpleadoResource(resources.ModelResource):
    class Meta:
        model = Empleado
        exclude = ('user', 'id')
        skip_unchanged = True
        report_skipped = True
        import_id_fields = ['Id_Empleado']


class ComputadoraResource(resources.ModelResource):
    class Meta:
        skip_unchanged = True
        report_skipped = True
        model = Computadora
        exclude = ('qr_code', 'id')
        import_id_fields = ['no_Serie_Co']

class Proyecto_empleadoResource(resources.ModelResource):
    class Meta:
        model=Proyecto_empleado
        skip_unchanged=True
        report_skipped=True
        exclude=('qr_code','id')
        import_id_fields = ['no_Serie_Mo']

class TecladoResource(resources.ModelResource):
    class Meta:
        model=Teclado
        skip_unchanged=True
        report_skipped=True
        exclude = ('qr_code','id')
        import_id_fields = ['no_Serie_Te']

class MouseResource(resources.ModelResource):
    class Meta:
        model=Mouse
        skip_unchanged = True
        report_skipped = True
        exclude = ('qr_code', 'id')
        import_id_fields = ['no_Serie_Mo']

class MonitorResource(resources.ModelResource):
    class Meta:
        model = Monitor
        skip_unchanged = True
        report_skipped = True
        exclude = ('qr_code', 'id')
        import_id_fields = ['no_Serie_Pa']


class Prestamo_ComputadoraResource(resources.ModelResource):
    class Meta:
        model = Prestamo_Computadora
        
class ImpresoraResource(resources.ModelResource):
    class Meta:
        model = Impresora
        skip_unchanged = True
        report_skipped = True
        exclude = ('qr_code', 'id')
        import_id_fields = ['no_Serie_Im']

class CelularResource(resources.ModelResource):
    class Meta:
        model = Celular
        skip_unchanged = True
        report_skipped = True
        exclude = ('qr_code', 'id')
        import_id_fields = ['no_Serie_Cel']

class RadioResource(resources.ModelResource):
    class Meta:
        model = Radio
        skip_unchanged = True
        report_skipped = True
        exclude = ('qr_code', 'id')
        import_id_fields = ['no_Serie_Rad']


class Prestamo_ImpresorasResource(resources.ModelResource):
    class Meta:
        model = Prestamo_Impresoras


class Prestamo_CelularResource(resources.ModelResource):
    class Meta:
        model = Prestamo_Celular


class Prestamo_RadioResource(resources.ModelResource):
    class Meta:
        model = Prestamo_Radio


class MultifuncionalResource(resources.ModelResource):
    class Meta:
        model = Multifuncional
        skip_unchanged = True
        report_skipped = True
        exclude = ('qr_code', 'id')
        import_id_fields = ['no_Serie_Mul']


class ProyectorResource(resources.ModelResource):
    class Meta:
        model = Proyector
        skip_unchanged = True
        report_skipped = True
        exclude = ('qr_code', 'id')
        import_id_fields = ['no_Serie_Pro']


class Eq_VidResource(resources.ModelResource):
    class Meta:
        model = Eq_Vid
        skip_unchanged = True
        report_skipped = True
        exclude = ('qr_code', 'id')
        import_id_fields = ['no_Serie_Vid']


class Prestamo_Eq_PubResource(resources.ModelResource):
    class Meta:
        model = Prestamo_Eq_Pub


class Clave_ImpresionResource(resources.ModelResource):
    class Meta:
        model = Clave_Impresion
        skip_unchanged = True
        report_skipped = True
        exclude = ('qr_code', 'id')
        import_id_fields = ['clave']




        














    

        








        
        

