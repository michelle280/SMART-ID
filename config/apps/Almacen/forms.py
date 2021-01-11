from django import forms
from apps.Almacen.models import *
import datetime
import django.forms.utils
import django.forms.widgets
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy 
#from betterforms.multiform import MultiModelForm
#from betterforms.forms import BaseForm
from django.views.decorators.http import require_GET

App_Choices = (
    ('ERP', 'SAP 7.4'),
    ('Costos', 'Costos unitarios'),
    ('Autocad', 'Autocad 2018'),
    ('Adobe reader', 'Adobe'),
    ('VPN', 'Cliente VPN'),
    ('DoPDF', 'DoPDF'),
    ('7-zip', '7-zip'),
    ('Control', 'Software de control Proyecto'),
    ('Diagramación', 'Software de diagramación'),
)

class Solicitud_ComputadorasForm(forms.ModelForm):
    Aplicaciones = forms.MultipleChoiceField(
        choices=App_Choices, widget=forms.CheckboxSelectMultiple,)
   
    class Meta:
        model = Solicitud_Equipo
        fields ="__all__"
        


class Peticion_Impresiones_ColorForm(forms.ModelForm):
     class Meta:
        model = Peticion_Impresiones_Color
        fields = "__all__"
        help_texts = {'fecha': ('Ingresa la fecha de hoy.'), }


class Ordenes_ServicioForm(forms.ModelForm):
     class Meta:
        model = Ordenes_Servicio
        fields = ['nombre_Emp','ApellidoP_Emp','ApellidoM_Emp','Proyecto','Area','clasificacion_equipo','reporte_usuario']

tipo_incidenciaChoices=(
    ('Videoconferencias','Videoconferencias'),
    ('Impresoras','Impresoras'),
    ('Correo Electrónico','Correo Electrónico'),
    ('Office','Office'),
    ('SAP','SAP'),
    ('Otro','Otro'),


)

class Incidencias_Rapidas(forms.Form):
    nombre=forms.CharField(required=True,max_length=30)
    aplellido_Paterno = forms.CharField(required=True, max_length=30)
    aplellido_Materno = forms.CharField(required=True, max_length=30)
    Tipo=forms.ChoiceField(choices=tipo_incidenciaChoices)
    mensaje=forms.CharField(widget=forms.Textarea())
    
    
    








