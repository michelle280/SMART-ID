from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import Context,Template
from django.contrib.auth import forms
from apps.Almacen.models import *
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm
from django.contrib.auth import login, logout,authenticate
from django.contrib import messages
from django.views.generic import FormView,ListView,DetailView
from django.template.loader import get_template
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from apps.Almacen.forms import*
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from webpush import send_user_notification
import json
from django.core.mail import BadHeaderError, send_mail
from twilio.twiml.messaging_response import MessagingResponse
from django_twilio.decorators import twilio_view
from django_twilio.request import decompose
from reportlab.pdfgen import canvas 



#Notificaciones Push





#Create your views here.

def HomeView(request):
    return render(request, "index.html")



def sesion(request):
    if request.user.is_authenticated:
        return render(request, "sesion.html")
    # En otro caso redireccionamos al login
    return redirect('/login')
        


def acceder(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            usuario = authenticate(username=nombre_usuario, password=password)
            if usuario is not None:
                login(request, usuario)
                messages.success(request, F"Bienvenido de nuevo {nombre_usuario}")
                return redirect('Sesion')
            else:
                messages.error(request, "Los datos son incorrectos")
        else:
            messages.error(request, "Los datos son incorrectos")
    form=AuthenticationForm()
    return render(request,"acceso.html",{"form":form})


def salir(request):
    logout(request)
    messages.success(request, F"Cesion cerrada")
    return redirect("acceder")



class crear_cuenta(View):

    def get(self, request):
        form = UserCreationForm()
        return render(request, "login.html", {"form": form})
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            nombre_usuario = form.cleaned_data.get("username")
            messages.success(request, F"Bienvenido a la plataforma {nombre_usuario}")
            login(request, usuario)
            return redirect("Sesion")
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            return render(request, "login.html")


class ComputadoraFormView(FormView):
    form_class = Solicitud_ComputadorasForm
    template_name='solicitudes_equipo.html'
    def get_success_url(self):
        return self.request.path
    def  form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.INFO,
                             "Se ha enviado tu solicitud")
        return super().form_valid(form)
    def form_invalid(self,form):
        form.add_error(None, "Tu información no es correcta,intenta de nuevo")
        return super().form_invalid(form)

class Peticion_Impresiones_ColorFormView(FormView):
    form_class = Peticion_Impresiones_ColorForm
    template_name = 'peticion_impresiones.html'
    

    def get_success_url(self):
        return self.request.path

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.INFO,
                             "Se ha enviado tu solicitud")
        return super().form_valid(form)

    def form_invalid(self, form):
        form.add_error(None, "Tu información no es correcta,intenta de nuevo")
        return super().form_invalid(form)


class Ordenes_ServicioFormFormView(FormView):
    form_class = Ordenes_ServicioForm
    template_name = 'Ordenes_ServicioForm.html'

    def get_success_url(self):
        return self.request.path

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.INFO,
                             "Se ha enviado tu solicitud")
        return super().form_valid(form)

    def form_invalid(self, form):
        form.add_error(None, "Tu información no es correcta,intenta de nuevo")
        return super().form_invalid(form)


class Contacto_directoListView(ListView):
    model=Contacto_directo
    template_name='contacts.html'
    








