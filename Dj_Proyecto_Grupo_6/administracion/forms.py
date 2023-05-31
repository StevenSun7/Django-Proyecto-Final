from django.forms import ModelForm, forms
from .models import contacto


class ContactoForm(forms.ModelForm):
    class Meta:
        model = contacto
        fields = ['apellido', 'nombre', 'email', 'telefono', 'consulta', 'comentario']
        # fields = '__all__'
