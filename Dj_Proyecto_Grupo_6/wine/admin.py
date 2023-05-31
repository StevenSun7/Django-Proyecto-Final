from django.contrib import admin
from wine.models import contacto,Categoria, Precio, Producto, Stock

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Precio)
admin.site.register(Producto)
admin.site.register(Stock)