from django import forms
from .models import Vehiculo,Cliente
Persona_Tipo = (
    ('fiscal', 'Juridica'),
    ('final', 'Fisica'),
)



class RentaForm(forms.ModelForm):

    vehiculo = forms.ModelChoiceField(queryset = Vehiculo.objects.filter(estado=True) )


