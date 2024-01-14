from django.shortcuts import render, redirect
from .models import Marca, Modelo, Vehiculo
from .forms import CrearVehiculoForm, EditarVehiculoForm
from django.db.models import Q

# Este metodo consiste en la consulta de todos los coches de la base de datos para poder
# mostrarlos en la tabla general del catalogo, delveremos el resultado de la consulta a
# la template catalogo.html
def consultar_vehiculos(request):
    vehiculos = Vehiculo.objects.select_related('idmarca', 'idmodelo').all()

    for vehiculo in vehiculos:
        print(f"ID: {vehiculo.idVehiculo}, Color: {vehiculo.color}, Marca: {vehiculo.idmarca.nombre}, Modelo: {vehiculo.idmodelo.nombre_modelo}, Puertas: {vehiculo.idmodelo.numero_puertas}, Motor: {vehiculo.idmodelo.tipo_motor}, Precio: {vehiculo.precio}")

    return render(request, 'catalogo.html', {'vehiculos': vehiculos})

# Este metodo consiste en la creacion de un vehiculo es decir en la insercion a la base
# de datos estos datos se insertaran desde el form corespondiente.
def crear_vehiculo(request):
    if request.method == 'POST':
        vehiculo_form = CrearVehiculoForm(request.POST)
        if vehiculo_form.is_valid():
            vehiculo_form.save()
            return redirect('consultar_vehiculos')
    else:
        vehiculo_form = CrearVehiculoForm()
    return render(request, "crearVehiculo.html", {'vehiculo_form':vehiculo_form})

# Este metodo consiste en la busqueda de vehiculos por ciertos atributos en concreto
# como se ve buscamos por cada uno de los atributos de las tablas permitiendo asi el
# no tener que poner filtros si no que usamos el filter de Django.
def buscar_por_nombre(request):
    if request.method == 'POST':
        query = request.POST.get('busqueda')
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
        vehiculos = Vehiculo.objects.all()
        return render(request, 'index.html', {'vehiculos': vehiculos})

# Este metodo consiste en el delete de un vehiculo.
def eliminar_vehiculo(request, idVehiculo):
    vehiculo = Vehiculo.objects.get(idVehiculo=idVehiculo)
    vehiculo.delete()
    return redirect('consultar_vehiculos')

# Este metodo consiste en el update de un vehiculo, como se programa en el form no se 
# podran editar todos los campos.
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
