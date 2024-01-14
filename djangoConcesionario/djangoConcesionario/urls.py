"""
URL configuration for djangoConcesionario project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path
from concesionario.views import buscar_por_nombre, consultar_vehiculos, crear_vehiculo, eliminar_vehiculo, editar_vehiculo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('catalogo/', consultar_vehiculos, name='consultar_vehiculos'),
    path('crear_vehiculo/', crear_vehiculo, name='crear_vehiculo'),
    path('buscarPorNombre', buscar_por_nombre, name='buscar_por_nombre'),
    path('eliminar_vehiculo/<int:idVehiculo>', eliminar_vehiculo, name='eliminar_vehiculo'),
    path('editar_vehiculo/<int:idVehiculo>', editar_vehiculo, name='editar_vehiculo'),
]
