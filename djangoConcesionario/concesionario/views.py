from django.shortcuts import render
from .models import Coche  # Importa tu modelo Coche

def lista_coches(request):
    # Obtiene todos los coches de la base de datos
    coches = Coche.objects.all()

    # Pasa la lista de coches al template
    context = {'coches': coches}

    # Renderiza el template y devuelve la respuesta
    return render(request, 'concesionario/lista_coches.html', context)
