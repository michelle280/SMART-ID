from django.contrib import admin
from apps.Almacen.models import *

admin.site.site_header="SMART-ID"

class AreaAdmin(admin.ModelAdmin):
    pass


admin.site.register(Area, AreaAdmin)

class EmpleadoAdmin(admin.ModelAdmin):
    search_fields = ("Id_Empleado", "nombre_Emp", 
                     "ApellidoP_Emp", "ApellidoP_Emp", "ApellidoM_Emp", "puesto", "correo_Emp")
    list_filter = ("Office","Area")
    list_display = ("nombre_Emp","ApellidoP_Emp","ApellidoM_Emp")
admin.site.register(Empleado,EmpleadoAdmin)

class ProyectoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Proyecto, ProyectoAdmin)



class Proyecto_empleadoAdmin(admin.ModelAdmin):
    search_fields = ("empleado", "Proyecto", "fecha_ingreso", "fecha_egreso")
    list_display = ("empleado", "Proyecto", "fecha_ingreso", "fecha_egreso")
    list_filter = ("fecha_ingreso", "fecha_egreso",  "Proyecto",)
    date_hierarchy = "fecha_ingreso"
    

admin.site.register(Proyecto_empleado, Proyecto_empleadoAdmin)

class ComputadoraAdmin(admin.ModelAdmin):
    search_fields = ("no_Serie_Co", "nombre_Co")
    list_filter=("Status","tipo_com","Ano")
    list_display = ("nombre_Co","Status","tipo_com")


admin.site.register(Computadora, ComputadoraAdmin)

class TecladoAdmin(admin.ModelAdmin):
    search_fields = ("computadora", "no_Serie_Te", "nombre_Te")
    list_filter = ("tipo_entrada",)
    list_display = ("computadora", "nombre_Te")

admin.site.register(Teclado,TecladoAdmin)


class MouseAdmin(admin.ModelAdmin):
    search_fields = ("computadora", "no_Serie_Mo", "nombre_Mo")
    list_filter = ("tipo_entrada",)
    list_display = ("computadora", "nombre_Mo")

admin.site.register(Mouse,MouseAdmin)

class MonitorAdmin(admin.ModelAdmin):
    search_fields = ("computadora", "no_Serie_Pa", "nombre_Pa")
    list_display = ("computadora", "no_Serie_Pa")


admin.site.register(Monitor, MonitorAdmin)


class Prestamo_ComputadoraAdmin(admin.ModelAdmin):
    search_fields = ("empleado", "computadora", "fecha_inicio", "fecha_fin")
    list_filter = ("fecha_inicio", "fecha_fin")
    list_display = ("empleado", "computadora")


admin.site.register(Prestamo_Computadora, Prestamo_ComputadoraAdmin)


class ImpresorasAdmin(admin.ModelAdmin):
    search_fields = ("no_Serie_Im", "nombre_Im")
    list_filter=("Status",)
    list_display = ("nombre_Im", "Status")


admin.site.register(Impresora, ImpresorasAdmin)


class CelularAdmin(admin.ModelAdmin):
    search_fields = ("no_Serie_Cel", "nombre_Cel")
    list_filter = ("Status",)
    list_display = ("nombre_Cel", "Status")


admin.site.register(Celular, CelularAdmin)


class RadioAdmin(admin.ModelAdmin):
    search_fields = ("no_Serie_Rad", "nombre_Rad")
    list_filter = ("Status",)
    list_display = ("nombre_Rad", "Status")


admin.site.register(Radio, RadioAdmin)

class Prestamo_ImpresorasAdmin(admin.ModelAdmin):
    search_fields = ("empleado", "Impresora", "fecha_inicio", "fecha_fin")
    list_filter = ("fecha_inicio", "fecha_fin",)
    list_display = ("empleado", "Impresora")


admin.site.register(Prestamo_Impresoras,Prestamo_ImpresorasAdmin)


class Prestamo_CelularAdmin(admin.ModelAdmin):
    search_fields = ("empleado", "celular", "fecha_inicio", "fecha_fin")
    list_filter = ("fecha_inicio", "fecha_fin",)
    list_display = ("empleado", "celular")


admin.site.register(Prestamo_Celular, Prestamo_CelularAdmin)

class Prestamo_RadioAdmin(admin.ModelAdmin):
    search_fields = ("empleado", "Radio", "fecha_inicio", "fecha_fin")
    list_filter = ("fecha_inicio", "fecha_fin",)
    list_display = ("empleado", "Radio")

admin.site.register(Prestamo_Radio, Prestamo_RadioAdmin)


class MultifuncionalAdmin(admin.ModelAdmin):
    search_fields = ("no_Serie_Mul", "nombre_Mul")
    list_filter = ("Status",)
    list_display = ("nombre_Mul", "Status")


admin.site.register(Multifuncional, MultifuncionalAdmin)


class ProyectorAdmin(admin.ModelAdmin):
    search_fields = ("no_Serie_Pro", "nombre_Pro")
    list_filter = ("Status",)
    list_display = ("nombre_Pro", "Status")


admin.site.register(Proyector, ProyectorAdmin)


class Eq_VidAdmin(admin.ModelAdmin):
    search_fields = ("no_Serie_Vid", "nombre_Vid")
    list_filter = ("Status",)
    list_display = ("nombre_Vid", "Status")


admin.site.register(Eq_Vid, Eq_VidAdmin)


class Prestamo_Eq_PubAdmin(admin.ModelAdmin):
    list_display = ("Proyecto", "Responsable", "Eq_Video","Proyector", "Multifuncional")
    list_filter = ("fecha_inicio", "fecha_fin",)
    search_fields = ("Proyecto", "Responsable", "Eq_Video","Proyector", "Multifuncional")


admin.site.register(Prestamo_Eq_Pub, Prestamo_Eq_PubAdmin)






