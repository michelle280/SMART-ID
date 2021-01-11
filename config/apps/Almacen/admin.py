from django.contrib import admin
from apps.Almacen.models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from apps.Almacen.resources import*


admin.site.site_header="SMART-ID"

class AreaAdmin(admin.ModelAdmin):
    pass


admin.site.register(Area, AreaAdmin)




class EmpleadoAdmin (ImportExportModelAdmin, admin.ModelAdmin):       
    
    search_fields = ("Id_Empleado", "nombre_Emp", 
                     "ApellidoP_Emp", "ApellidoM_Emp", "puesto", "correo_Emp")
    list_filter = ("Office","Area")
    list_display = ("nombre_Emp","ApellidoP_Emp","ApellidoM_Emp")
    resource_class=EmpleadoResource
  
admin.site.register(Empleado, EmpleadoAdmin)



class ProyectoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Proyecto, ProyectoAdmin)


class Proyecto_empleadoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ("empleado", "Proyecto", "fecha_ingreso", "fecha_egreso")
    list_display = ("empleado", "Proyecto", "fecha_ingreso", "fecha_egreso")
    list_filter = ("fecha_ingreso", "fecha_egreso",  "Proyecto",)
    date_hierarchy = "fecha_ingreso"
    resource_class = Proyecto_empleadoResource
    

admin.site.register(Proyecto_empleado, Proyecto_empleadoAdmin)

class ComputadoraAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ("no_Serie_Co", "nombre_Co")
    list_filter=("Status","tipo_com","Ano")
    list_display = ("nombre_Co","Status","tipo_com")
    resource_class = ComputadoraResource
    actions = ["cambiar_status_a_disponible",
               "cambiar_status_a_reparacion", "cambiar_status_a_destruccion", "cambiar_status_a_en_servicio"]
    def  cambiar_status_a_disponible(self,request,queryset):
       queryset.update(Status="disponible")

    def cambiar_status_a_reparacion(self, request, queryset):
        queryset.update(Status="reparacion")

    def cambiar_status_a_destruccion(self, request, queryset):
        queryset.update(Status="destruccion")

    def cambiar_status_a_en_servicio(self, request, queryset):
        queryset.update(Status="servicio")
    
    



admin.site.register(Computadora, ComputadoraAdmin)



class TecladoAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ("computadora", "no_Serie_Te", "nombre_Te")
    list_filter = ("tipo_entrada",)
    list_display = ("computadora", "nombre_Te")
    resource_class = TecladoResource

admin.site.register(Teclado,TecladoAdmin)


class MouseAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ("computadora", "no_Serie_Mo", "nombre_Mo")
    list_filter = ("tipo_entrada",)
    list_display = ("computadora", "nombre_Mo")
    resource_class=MouseResource

admin.site.register(Mouse,MouseAdmin)


class MonitorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ("computadora", "no_Serie_Pa", "nombre_Pa")
    list_display = ("computadora", "no_Serie_Pa")
    resource_class = MonitorResource


admin.site.register(Monitor, MonitorAdmin)


class ImpresorasAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ("no_Serie_Im", "nombre_Im")
    list_filter=("Status",)
    list_display = ("nombre_Im", "Status")
    resource_class = ImpresoraResource
    actions = ["cambiar_status_a_disponible",
               "cambiar_status_a_reparacion", "cambiar_status_a_destruccion", "cambiar_status_a_en_servicio"]

    def cambiar_status_a_disponible(self, request, queryset):
       queryset.update(Status="disponible")

    def cambiar_status_a_reparacion(self, request, queryset):
        queryset.update(Status="reparacion")

    def cambiar_status_a_destruccion(self, request, queryset):
        queryset.update(Status="destruccion")

    def cambiar_status_a_en_servicio(self, request, queryset):
        queryset.update(Status="servicio")


admin.site.register(Impresora, ImpresorasAdmin)


class CelularAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ("no_Serie_Cel", "nombre_Cel")
    list_filter = ("Status",)
    list_display = ("nombre_Cel", "Status")
    resource_class = CelularResource
    actions = ["cambiar_status_a_disponible",
               "cambiar_status_a_reparacion", "cambiar_status_a_destruccion", "cambiar_status_a_en_servicio"]
    def cambiar_status_a_disponible(self, request, queryset):
           queryset.update(Status="disponible")

    def cambiar_status_a_reparacion(self, request, queryset):
        queryset.update(Status="reparacion")

    def cambiar_status_a_destruccion(self, request, queryset):
        queryset.update(Status="destruccion")

    def cambiar_status_a_en_servicio(self, request, queryset):
        queryset.update(Status="servicio")


admin.site.register(Celular, CelularAdmin)


class RadioAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ("no_Serie_Rad", "nombre_Rad")
    list_filter = ("Status",)
    list_display = ("nombre_Rad", "Status")
    resource_class = RadioResource
    actions = ["cambiar_status_a_disponible",
               "cambiar_status_a_reparacion", "cambiar_status_a_destruccion", "cambiar_status_a_en_servicio"]

    def cambiar_status_a_disponible(self, request, queryset):
        queryset.update(Status="disponible")

    def cambiar_status_a_reparacion(self, request, queryset):
        queryset.update(Status="reparacion")

    def cambiar_status_a_destruccion(self, request, queryset):
        queryset.update(Status="destruccion")

    def cambiar_status_a_en_servicio(self, request, queryset):
        queryset.update(Status="servicio")


admin.site.register(Radio, RadioAdmin)


class Prestamo_ImpresorasAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ("empleado", "Impresora", "fecha_inicio", "fecha_fin")
    list_filter = ("fecha_inicio", "fecha_fin",)
    list_display = ("empleado", "Impresora")
    resource_class = Prestamo_ImpresorasResource


admin.site.register(Prestamo_Impresoras,Prestamo_ImpresorasAdmin)


class Prestamo_CelularAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ("empleado", "celular", "fecha_inicio", "fecha_fin")
    list_filter = ("fecha_inicio", "fecha_fin",)
    list_display = ("empleado", "celular")
    resource_class = Prestamo_CelularResource


admin.site.register(Prestamo_Celular, Prestamo_CelularAdmin)

class Prestamo_RadioAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ("empleado", "Radio", "fecha_inicio", "fecha_fin")
    list_filter = ("fecha_inicio", "fecha_fin",)
    list_display = ("empleado", "Radio")
    resource_class = Prestamo_RadioResource

admin.site.register(Prestamo_Radio, Prestamo_RadioAdmin)


class MultifuncionalAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ("no_Serie_Mul", "nombre_Mul")
    list_filter = ("Status",)
    list_display = ("nombre_Mul", "Status")
    resource_class = MultifuncionalResource
    actions = ["cambiar_status_a_disponible",
               "cambiar_status_a_reparacion", "cambiar_status_a_destruccion", "cambiar_status_a_en_servicio"]

    def cambiar_status_a_disponible(self, request, queryset):
        queryset.update(Status="disponible")

    def cambiar_status_a_reparacion(self, request, queryset):
        queryset.update(Status="reparacion")

    def cambiar_status_a_destruccion(self, request, queryset):
        queryset.update(Status="destruccion")

    def cambiar_status_a_en_servicio(self, request, queryset):
        queryset.update(Status="servicio")


admin.site.register(Multifuncional, MultifuncionalAdmin)


class ProyectorAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ("no_Serie_Pro", "nombre_Pro")
    list_filter = ("Status",)
    list_display = ("nombre_Pro", "Status")
    resource_class = ProyectorResource


admin.site.register(Proyector, ProyectorAdmin)


class Eq_VidAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ("no_Serie_Vid", "nombre_Vid")
    list_filter = ("Status",)
    list_display = ("nombre_Vid", "Status")
    resource_class = Eq_VidResource
    actions = ["cambiar_status_a_disponible",
               "cambiar_status_a_reparacion", "cambiar_status_a_destruccion", "cambiar_status_a_en_servicio"]

    def cambiar_status_a_disponible(self, request, queryset):
        queryset.update(Status="disponible")

    def cambiar_status_a_reparacion(self, request, queryset):
        queryset.update(Status="reparacion")

    def cambiar_status_a_destruccion(self, request, queryset):
        queryset.update(Status="destruccion")

    def cambiar_status_a_en_servicio(self, request, queryset):
        queryset.update(Status="servicio")


admin.site.register(Eq_Vid, Eq_VidAdmin)


class Solicitud_EquipoAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ("nombre_Emp", "ApellidoP_Emp",
                     "ApellidoM_Emp")
    list_filter = ("Area", "Fecha_inicio", "tipo_com",
                   "monitor", "Office","teclado", "Status", "Proyecto",)
    list_display = ("nombre_Emp", "ApellidoP_Emp",
                    "ApellidoM_Emp", "Fecha_inicio", "Status")
    resource_class = Prestamo_Eq_PubResource


admin.site.register(Solicitud_Equipo, Solicitud_EquipoAdmin)



class Peticion_Impresiones_ColorAdmin(admin.ModelAdmin):
    list_display = ("nombre_Emp", "ApellidoP_Emp",
                    "ApellidoM_Emp", "saldo")
    list_filter = ("Fecha",)
    search_fields = ("nombre_Emp", "ApellidoP_Emp",
                     "ApellidoM_Emp", "Area")
     

admin.site.register(Peticion_Impresiones_Color,Peticion_Impresiones_ColorAdmin)


class Clave_ImpresionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = Clave_ImpresionResource
    search_fields = ("empleado","clave")


admin.site.register(Clave_Impresion, Clave_ImpresionAdmin)






