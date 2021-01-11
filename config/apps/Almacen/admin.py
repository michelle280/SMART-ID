from django.contrib import admin
from apps.Almacen.models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from apps.Almacen.resources import*
from django.db.models.functions import TruncDay
from django.db.models import Count
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.admin import site
import adminactions.actions as actions
from admin_adv_search_builder.filters import AdvancedSearchBuilder
from adminsortable2.admin import SortableAdminMixin

#from ajax_select import make_ajax_form

#from massadmin import mass_change_selected




admin.site.site_header="SMART-ID"

#site.add_action(mass_change_selected)


site.add_action(actions.graph_queryset)
#site.add_action(actions.export_as_xls)

class AreaAdmin(admin.ModelAdmin):
    actions=None

    


admin.site.register(Area, AreaAdmin)


class EmpleadoAdmin (ImportExportModelAdmin, admin.ModelAdmin):

    search_fields = ("Id_Empleado", "nombre_Emp", 
                     "ApellidoP_Emp", "ApellidoM_Emp", "puesto", "correo_Emp")
    list_filter = ("Office", "Area")
    list_display = ("nombre_Emp","ApellidoP_Emp","ApellidoM_Emp")
    resource_class=EmpleadoResource
    massadmin_exclude = ["nombre_Emp", "ApellidoP_Emp",
                         "ApellidoM_Emp", "Id_Empleado", "Area"]
    actions = [actions.export_as_xls]
    

  
admin.site.register(Empleado, EmpleadoAdmin)



class ProyectoAdmin(admin.ModelAdmin):
    massadmin_exclude = ["Id_proyecto","nombre_proyecto","direccion"]
    search_fields=[AdvancedSearchBuilder,"Id_proyecto","nombre_proyecto","direccion"]
    

    
    

admin.site.register(Proyecto, ProyectoAdmin)


class Proyecto_empleadoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ("empleado", "Proyecto", "fecha_ingreso", "fecha_egreso")
    list_display = ("empleado", "Proyecto", "fecha_ingreso", "fecha_egreso")
    list_filter = (AdvancedSearchBuilder,"fecha_ingreso", "fecha_egreso",  "Proyecto",)
    date_hierarchy = "fecha_ingreso"
    resource_class = Proyecto_empleadoResource
    autocomplete_fields = ["empleado","Proyecto"]
   

    actions = [actions.export_as_xls]


admin.site.register(Proyecto_empleado, Proyecto_empleadoAdmin)

class ComputadoraAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ("no_Serie_Co", "nombre_Co")
    list_filter = (AdvancedSearchBuilder, "Status", "tipo_com", "Ano")
    list_display = ("nombre_Co","Status","tipo_com")
    resource_class = ComputadoraResource
    actions = ["cambiar_status_a_disponible",
               "cambiar_status_a_reparacion", "cambiar_status_a_destruccion", "cambiar_status_a_en_servicio", actions.export_as_xls, actions.graph_queryset]
    massadmin_exclude = ["Ano", "tipo_com", "no_Serie_Co",
                         "qr_code", "nombre_Co", "marca", "modelo_com", "Procesador"]
    save_as = True
    save_on_top = True
   
    
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
    list_filter = (AdvancedSearchBuilder, "tipo_entrada",)
    list_display = ("computadora", "nombre_Te")
    resource_class = TecladoResource
    actions = [actions.export_as_xls, actions.graph_queryset]
    autocomplete_fields=["computadora"]
    

admin.site.register(Teclado,TecladoAdmin)


class MouseAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ("computadora", "no_Serie_Mo", "nombre_Mo")
    list_filter = (AdvancedSearchBuilder, "tipo_entrada",)
    list_display = ("computadora", "nombre_Mo")
    resource_class=MouseResource
    actions = [actions.export_as_xls, actions.graph_queryset]
    autocomplete_fields=["computadora"]

admin.site.register(Mouse,MouseAdmin)


class MonitorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = (AdvancedSearchBuilder,"computadora", "no_Serie_Pa", "nombre_Pa")
    list_display = ("computadora", "no_Serie_Pa")
    resource_class = MonitorResource
    actions = [actions.export_as_xls, actions.graph_queryset]
    autocomplete_fields = ["computadora"]


admin.site.register(Monitor, MonitorAdmin)


class ImpresorasAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ("no_Serie_Im", "nombre_Im")
    list_filter = (AdvancedSearchBuilder, "Status",)
    list_display = ("nombre_Im", "Status")
    resource_class = ImpresoraResource
    actions = ["cambiar_status_a_disponible",
               "cambiar_status_a_reparacion", "cambiar_status_a_destruccion", "cambiar_status_a_en_servicio", actions.export_as_xls, actions.graph_queryset]

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
    list_filter = (AdvancedSearchBuilder,"Status",)
    list_display = ("nombre_Cel", "Status")
    resource_class = CelularResource
    actions = ["cambiar_status_a_disponible",
               "cambiar_status_a_reparacion", "cambiar_status_a_destruccion", "cambiar_status_a_en_servicio", actions.export_as_xls, actions.graph_queryset]
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
    list_filter = (AdvancedSearchBuilder, "Status",)
    list_display = ("nombre_Rad", "Status")
    resource_class = RadioResource
    actions = ["cambiar_status_a_disponible",
               "cambiar_status_a_reparacion", "cambiar_status_a_destruccion", "cambiar_status_a_en_servicio", actions.export_as_xls, actions.graph_queryset]

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
    list_filter = (AdvancedSearchBuilder, "fecha_inicio", "fecha_fin",)
    list_display = ("empleado", "Impresora")
    autocomplete_fields=["empleado", "Impresora"]
    actions = [actions.export_as_xls]
    resource_class = Prestamo_ImpresorasResource


admin.site.register(Prestamo_Impresoras,Prestamo_ImpresorasAdmin)


class Prestamo_CelularAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ("empleado", "celular", "fecha_inicio", "fecha_fin")
    list_filter = (AdvancedSearchBuilder, "fecha_inicio", "fecha_fin",)
    list_display = ("empleado", "celular")
    resource_class = Prestamo_CelularResource
    actions = [actions.export_as_xls]
    autocomplete_fields=["empleado", "celular"]


admin.site.register(Prestamo_Celular, Prestamo_CelularAdmin)


class Prestamo_ComputadoraAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ("empleado", "computadora", "fecha_inicio", "fecha_fin")
    list_filter = (AdvancedSearchBuilder, "fecha_inicio", "fecha_fin",)
    list_display = ("empleado", "computadora")
    resource_class = Prestamo_CelularResource
    actions = [actions.export_as_xls]
    autocomplete_fields = ["empleado", "computadora"]


admin.site.register(Prestamo_Computadora, Prestamo_ComputadoraAdmin)



class Prestamo_RadioAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ("empleado", "Radio", "fecha_inicio", "fecha_fin")
    list_filter = (AdvancedSearchBuilder,"fecha_inicio", "fecha_fin",)
    list_display = ("empleado", "Radio")
    resource_class = Prestamo_RadioResource
    actions = [actions.export_as_xls]
    autocomplete_fields=["empleado", "Radio"]

admin.site.register(Prestamo_Radio, Prestamo_RadioAdmin)


class MultifuncionalAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ("no_Serie_Mul", "nombre_Mul")
    list_filter = (AdvancedSearchBuilder, "Status",)
    list_display = ("nombre_Mul", "Status")
    resource_class = MultifuncionalResource
    actions = ["cambiar_status_a_disponible",
               "cambiar_status_a_reparacion", "cambiar_status_a_destruccion", "cambiar_status_a_en_servicio",  actions.export_as_xls, actions.graph_queryset]

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
    list_filter = (AdvancedSearchBuilder,"Status",)
    list_display = ("nombre_Pro", "Status")
    resource_class = ProyectorResource
    actions = [actions.export_as_xls, actions.graph_queryset]


admin.site.register(Proyector, ProyectorAdmin)


class Eq_VidAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ("no_Serie_Vid", "nombre_Vid")
    list_filter = (AdvancedSearchBuilder, "Status",)
    list_display = ("nombre_Vid", "Status")
    resource_class = Eq_VidResource
    actions = ["cambiar_status_a_disponible",
               "cambiar_status_a_reparacion", "cambiar_status_a_destruccion", "cambiar_status_a_en_servicio", actions.export_as_xls, actions.graph_queryset]

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
    list_filter = (AdvancedSearchBuilder,"Area", "Fecha_inicio", "tipo_com",
                   "monitor", "Office","teclado", "Status", "Proyecto",)
    list_display = ("nombre_Emp", "ApellidoP_Emp",
                    "ApellidoM_Emp", "Fecha_inicio", "Status")
    
    change_list_template = 'admin/changepetieq.html'
    resource_class = Prestamo_Eq_PubResource
    actions = [actions.export_as_xls, actions.graph_queryset]


    def changelist_view(self, request, extra_context=None):
        # Listas por dia
        chart_data = (
            Solicitud_Equipo.objects.annotate(date=TruncDay("Fecha_inicio"))
            .values("date")
            .annotate(y=Count("id"))
            .order_by("-date")
        )

        # Serialize and attach the chart data to the template context
        as_json = json.dumps(list(chart_data), cls=DjangoJSONEncoder)
        extra_context = extra_context or {"chart_data": as_json}

        # Call the superclass changelist_view to render the page
        return super().changelist_view(request, extra_context=extra_context)


admin.site.register(Solicitud_Equipo, Solicitud_EquipoAdmin)



class Peticion_Impresiones_ColorAdmin(admin.ModelAdmin):
    list_display = ("nombre_Emp", "ApellidoP_Emp",
                    "ApellidoM_Emp", "saldo")
    list_filter = (AdvancedSearchBuilder, "Fecha",)
    search_fields = ("nombre_Emp", "ApellidoP_Emp",
                     "ApellidoM_Emp", "Area")
    change_list_template = 'admin/changepetciones.html'
    actions = [actions.export_as_xls, actions.graph_queryset]
    autocomplete_fields = ["Clave"]

    def changelist_view(self, request, extra_context=None):
        # Listas por dia
        chart_data = (
            Peticion_Impresiones_Color.objects.annotate(date=TruncDay("Fecha"))
            .values("date")
            .annotate(y=Count("id"))
            .order_by("-date")
        )

        # Serialize and attach the chart data to the template context
        as_json = json.dumps(list(chart_data), cls=DjangoJSONEncoder)
        extra_context = extra_context or {"chart_data": as_json}

        # Call the superclass changelist_view to render the page
        return super().changelist_view(request, extra_context=extra_context)
     

admin.site.register(Peticion_Impresiones_Color,Peticion_Impresiones_ColorAdmin)


class Clave_ImpresionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = Clave_ImpresionResource
    search_fields = ("empleado", "clave")
    list_filter = (AdvancedSearchBuilder,)
    actions = [actions.export_as_xls]
    


admin.site.register(Clave_Impresion, Clave_ImpresionAdmin)
class Orden_servicioAdmin(admin.ModelAdmin):
    search_fields = ("nombre_Emp", "ApellidoP_Emp",
                     "ApellidoM_Emp", "Area","Proyecto","Atencion")
    list_filter = (AdvancedSearchBuilder,"Area", "fecha_resolucion", "fecha_inicidencia", "clasificacion_equipo", "tipo_atencion", "dano_fisico", "retirar", "codigo_error", "Status", "Proyecto","Atencion",)
    list_display = ("nombre_Emp", "ApellidoP_Emp",
                    "ApellidoM_Emp", "clasificacion_equipo", "fecha_resolucion", "fecha_inicidencia", "Atencion")
    change_list_template = 'admin/changeOrdenesdeservicio.html'
    actions = [actions.export_as_xls, actions.graph_queryset]

    def changelist_view(self, request, extra_context=None):
        # Listas por dia
        chart_data = (
            Ordenes_Servicio.objects.annotate(
                date=TruncDay("fecha_inicidencia"))
            .values("date")
            .annotate(y=Count("id"))
            .order_by("-date")
        )

        # Serialize and attach the chart data to the template context
        as_json = json.dumps(list(chart_data), cls=DjangoJSONEncoder)
        extra_context = extra_context or {"chart_data": as_json}

        # Call the superclass changelist_view to render the page
        return super().changelist_view(request, extra_context=extra_context)


admin.site.register(Ordenes_Servicio, Orden_servicioAdmin)


class Contacto_directoAdmin(admin.ModelAdmin):
    search_fields = ("nombre", "numero_celular")
    list_filter = (AdvancedSearchBuilder, "nombre", "numero_celular",)
    list_display = ("nombre", "numero_celular")


admin.site.register(Contacto_directo, Contacto_directoAdmin)











