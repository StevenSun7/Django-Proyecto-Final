from django.forms import ModelForm, forms
from .models import contacto

class ContactoForm(ModelForm):
    class Meta:
        model = contacto
        fields = ['apellido', 'nombre', 'email', 'telefono', 'consulta', 'comentario']

    def clean_telefono(self):
        telefono = self.cleaned_data['telefono']
        if len(telefono) != 10:
            raise forms.ValidationError("El número de teléfono debe tener 10 dígitos.")
        return telefono
