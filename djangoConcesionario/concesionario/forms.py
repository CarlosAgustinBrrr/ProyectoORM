from django import forms
from .models import Marca, Modelo, Vehiculo
from django.core.validators import MinValueValidator

class CrearVehiculoForm(forms.ModelForm):
    precio = forms.FloatField(
        validators=[MinValueValidator(1, message='El precio debe ser mayor que 0')],
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
    )

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
            'idmarca': forms.Select(attrs={'class': 'form-control'}),
            'idmodelo': forms.Select(attrs={'class': 'form-control'}),
            'color': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        
class EditarVehiculoForm(forms.ModelForm):
    precio = forms.FloatField(
        validators=[MinValueValidator(1, message='El precio debe ser mayor que 0')],
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
    )
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
            'idmarca': forms.Select(attrs={'class':'form-control', 'disabled': True}),
            'idmodelo': forms.Select(attrs={'class':'form-control', 'disabled': True}),
            'color': forms.TextInput(attrs={'class':'form-control'}),
            'precio': forms.NumberInput(attrs={'class':'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(EditarVehiculoForm, self).__init__(*args, **kwargs)
        self.fields['idmarca'].disabled = True
        self.fields['idmodelo'].disabled = True