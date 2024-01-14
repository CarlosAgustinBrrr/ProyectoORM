from django import forms
from .models import Marca, Modelo, Vehiculo
from django.core.validators import MinValueValidator

# Este es el formulario para añadir vehiculos a la base de datos como podemos ver
# se controla mediante el validators que el precio se superior a 0, los demas datos
# menos el color estaran hardcodeados mediante dropdowns en el template.
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
        
# Este es el formulario de la edicion de vehiculos como se puede ver no se permiten 
# modificar todos los campos el idmarca y idmodelo no se pueden modificat solo colo
#y precio.
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