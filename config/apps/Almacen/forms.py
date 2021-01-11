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

class Solicitud_ComputadorasForm(forms.ModelForm):
    class Meta:
        model = Solicitud_Equipo
        fields ="__all__"
        


class Peticion_Impresiones_ColorForm(forms.ModelForm):
     class Meta:
        model = Peticion_Impresiones_Color
        fields = "__all__"
        help_texts = {'fecha': ('Ingresa la fecha de hoy.'), }





