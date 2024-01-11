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
from django.urls import path
from concesionario.views import consultar_vehiculos
from concesionario.views import crearVehiculo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', consultar_vehiculos, name='consultar_vehiculos'),
    path('crearVehiculo', crearVehiculo, name='crearVehiculo'),
]
