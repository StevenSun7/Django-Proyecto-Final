from django.db import models

# Create your models here.

class Categoria(models.Model):
    id_categoria = models.IntegerField(primary_key=True)
    nombre =  models.CharField(max_length=50)
    descripcion = models.CharField(max_length=250)
    
    
class Producto(models.Model):
    id_producto =  models.IntegerField(primary_key=True,unique=True)
    id_categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=250)
    conservacion = models.CharField(max_length=250)
    bodega = models.CharField(max_length=100, default='')
    
    
class Precio(models.Model):
    id_precio = models.IntegerField(primary_key=True)
    id_producto = models.ForeignKey(Producto,null=True, on_delete=models.SET_NULL)
    fe_desde =  models.DateField()
    fe_hasta =  models.DateField()
    precio = models.FloatField()
    desc_xcaja = models.FloatField()
    promo = models.FloatField()