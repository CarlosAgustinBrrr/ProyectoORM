from django.shortcuts import render, redirect
from .models import Marca, Modelo, Vehiculo
from .forms import VehiculoForm

def consultar_vehiculos(request):
    vehiculos = Vehiculo.objects.select_related('idmarca', 'idmodelo').all()

    for vehiculo in vehiculos:
        print(f"ID: {vehiculo.idVehiculo}, Color: {vehiculo.color}, Marca: {vehiculo.idmarca.nombre}, Modelo: {vehiculo.idmodelo.nombre_modelo}, Puertas: {vehiculo.idmodelo.numero_puertas}, Motor: {vehiculo.idmodelo.tipo_motor}, Precio: {vehiculo.precio}")

    return render(request, 'index.html', {'vehiculos': vehiculos})

def crear_vehiculo(request):
    if request.method == 'POST':
        vehiculo_form = VehiculoForm(request.POST)
        if vehiculo_form.is_valid():
            vehiculo_form.save()
            return redirect('consultar_vehiculos')
    else:
        vehiculo_form = VehiculoForm()
    return render(request, "crearVehiculo.html", {'vehiculo_form':vehiculo_form})
