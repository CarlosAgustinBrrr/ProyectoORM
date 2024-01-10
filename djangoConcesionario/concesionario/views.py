from django.shortcuts import render
from .models import Coche  # Importa tu modelo Coche

# Create your views here.

def index(request):
    return render(request, "index.html")