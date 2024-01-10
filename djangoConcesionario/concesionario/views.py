from django.shortcuts import render
from .models import Marca
from .models import Vehiculo
from .models import Modelo


# Create your views here.

def index(request):
    return render(request, "index.html")