from django.contrib import admin
from .models import Categoria, Precio, Producto
from wine.models import contacto

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Precio)
admin.site.register(Producto)
admin.site.register(contacto)
