from django.shortcuts import render, redirect
from .models import Marca, Modelo, Vehiculo
from .forms import VehiculoForm
from django.db.models import Q

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

def buscar_por_nombre(request):
    if request.method == 'POST':
        query = request.POST.get('busqueda')  # Obtén la consulta enviada desde el formulario

        # Filtrado en múltiples campos utilizando Q objects para hacer OR entre los campos.
        vehiculos = Vehiculo.objects.filter(
            Q(idVehiculo__icontains=query) |
            Q(idmarca__nombre__icontains=query) |
            Q(idmodelo__nombre_modelo__icontains=query) |
            Q(idmodelo__numero_puertas__icontains=query) |
            Q(idmodelo__tipo_motor__icontains=query) |
            Q(color__icontains=query) |
            Q(precio__icontains=query)
        )

        return render(request, 'index.html', {'vehiculos': vehiculos})
    else:
        # Si no es un POST, simplemente renderiza la página con todos los vehículos.
        vehiculos = Vehiculo.objects.all()
        return render(request, 'index.html', {'vehiculos': vehiculos})
    
def eliminar_vehiculo(request, idVehiculo):
    vehiculo = Vehiculo.objects.get(idVehiculo=idVehiculo)
    vehiculo.delete()

    vehiculos = Vehiculo.objects.all()
    return render(request, 'index.html', {'vehiculos': vehiculos})