from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import Context,Template
from django.contrib.auth import forms
from apps.Almacen.models import *
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages
#Create your views here.
def acceder(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            usuario = authenticate(username=nombre_usuario, password=password)
            if usuario is not None:
               login(request, usuario)
               messages.success(
                   request, F"Bienvenido de nuevo{nombre_usuario}")
               return redirect("index")
            else:
                messages.error(request, "Los datos son incorrectos")
        else:
            messages.error(request, "Los datos son incorrectos")
    form=AuthenticationForm()
    return render(request,"acceso.html",{"form":form})


def salir(request):
    logout(request)
    messages.success(request, F"Cesion cerrada{nombre_usuario}")
    return redirect(acceder)

def index(request):
    return render(request,'index.html')

class login(View):
    def get(self,request):
        form= UserCreationForm()
        return render(request,"login.html",{"form":form})

            
    def post(self,request):
        form=UserCreationForm(request.POST)
        if form.is_valid():
            usuario=form.save()
            nombre_usuario=form.cleaned_data.get("username")
            messages.success(request, F"Bienvenido a la plataforma {nombre_usuario}")
            login(request,usuario)
            return redirect("index")
        else:
            for msg in form.error_messages:
                messages.error(request,form.error_messages[msg])
        return render(request, "login.html",{"form": form})




#def login(request):
    #return render(request,"login.html")
    





