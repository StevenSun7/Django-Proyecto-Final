from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse(f"""<h1>Proyecto Django Grupo 6</h1>""")

def saludar(request, nombre):
    return HttpResponse(f"""<h1>Welcome {nombre} 🍷</h1>""")