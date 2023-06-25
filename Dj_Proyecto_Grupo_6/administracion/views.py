from django.shortcuts import render
from django.http import HttpResponse
from .models import Categoria
import html 

# Create your views here.
def lista(request):
    categoria = Categoria.objects.all()
    contenido_html = "<!DOCTYPE html><html><head><title>Ejemplo de HTML</title></head><body><h1>Título de la página</h1><p>Este es un ejemplo de HTML</p>"
    
    texto = "<table><tr><th>Categoria</th><th>nombre</th><th>descripcion</th></tr>"
    
    for categ in categoria:
        texto = texto + f"<tr><td>{categ.id_categoria}</td><td>{categ.nombre} </td><td>{categ.descripcion} </td></tr>"
        
    texto = texto + "</table>"
    
    return HttpResponse(texto, content_type='text/html')
