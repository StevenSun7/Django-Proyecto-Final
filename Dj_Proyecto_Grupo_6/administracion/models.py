from django.db import models

# Create your models here.

class Categoria(models.Model):
    id_categoria = models.IntegerField(unique=True)
    nombre =  models.CharField(max_length=50)
    descripcion = models.CharField(max_length=250)
    
    
class Producto(models.Model):
    id_producto =  models.IntegerField(unique=True)
    id_categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=250)
    conservacion = models.CharField(max_length=250)
    
class Precio(models.Model):
    id_precio = models.IntegerField(unique=True)
    id_producto = models.ForeignKey(Producto,null=True, on_delete=models.SET_NULL)
    fe_desde =  models.DateField()
    fe_hasta =  models.DateField()
    precio = models.FloatField()
    desc_xcaja = models.FloatField()
    promo = models.FloatField()