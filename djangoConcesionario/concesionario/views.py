from django.shortcuts import render
from .models import Marca, Modelo, Vehiculo
from .forms import VehiculoForm

# Create your views here.

def index(request):
    return render(request, "index.html")

def crearVehiculo(request):
    if request.method == 'POST':
        vehiculo_form = VehiculoForm(request.POST)
        if vehiculo_form.is_valid():
            vehiculo_form.save()
            return render(request, "index.html")
    else:
        vehiculo_form = VehiculoForm()
    return render(request, "crearVehiculo.html", {'vehiculo_form':vehiculo_form})