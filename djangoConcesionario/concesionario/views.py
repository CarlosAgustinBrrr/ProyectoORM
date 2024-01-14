from django.shortcuts import render, redirect
from .models import Marca, Modelo, Vehiculo
from .forms import CrearVehiculoForm, EditarVehiculoForm
from django.db.models import Q

def consultar_vehiculos(request):
    vehiculos = Vehiculo.objects.select_related('idmarca', 'idmodelo').all()

    for vehiculo in vehiculos:
        print(f"ID: {vehiculo.idVehiculo}, Color: {vehiculo.color}, Marca: {vehiculo.idmarca.nombre}, Modelo: {vehiculo.idmodelo.nombre_modelo}, Puertas: {vehiculo.idmodelo.numero_puertas}, Motor: {vehiculo.idmodelo.tipo_motor}, Precio: {vehiculo.precio}")

    return render(request, 'catalogo.html', {'vehiculos': vehiculos})

def crear_vehiculo(request):
    if request.method == 'POST':
        vehiculo_form = CrearVehiculoForm(request.POST)
        if vehiculo_form.is_valid():
            vehiculo_form.save()
            return redirect('consultar_vehiculos')
    else:
        vehiculo_form = CrearVehiculoForm()
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

        return render(request, 'catalogo.html', {'vehiculos': vehiculos})
    else:
        # Si no es un POST, simplemente renderiza la página con todos los vehículos.
        vehiculos = Vehiculo.objects.all()
        return render(request, 'catalogo.html', {'vehiculos': vehiculos})
    
def eliminar_vehiculo(request, idVehiculo):
    vehiculo = Vehiculo.objects.get(idVehiculo=idVehiculo)
    vehiculo.delete()
    return redirect('consultar_vehiculos')

def editar_vehiculo(request, idVehiculo):
    vehiculo = Vehiculo.objects.get(idVehiculo=idVehiculo)
    if request.method == 'POST':
        edit_form = EditarVehiculoForm(request.POST, instance=vehiculo)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('consultar_vehiculos')
    else:
        edit_form = EditarVehiculoForm(instance=vehiculo)
    return render(request, 'editarVehiculo.html', {'edit_form': edit_form})
