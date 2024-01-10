from django import forms
from .models import Marca, Modelo, Vehiculo

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['idmarca', 'idmodelo', 'color', 'precio']
        labels = {
            'idmarca': 'Marca',
            'idmodelo': 'Modelo',
            'color': 'Color',
            'precio': 'Precio',
        }
        widgets = {
            'idmarca': forms.Select(attrs={'class':'form-control'}),
            'idmodelo': forms.Select(attrs={'class':'form-control'}),
            'color': forms.TextInput(attrs={'class':'form-control'}),
            'precio': forms.NumberInput(attrs={'class':'form-control'}),
        }
        