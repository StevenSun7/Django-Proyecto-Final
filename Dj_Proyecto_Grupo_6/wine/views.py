from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView

## Modelos
from .models import Producto, Precio, Categoria

# Create your views here.
def index(request):
    if(request.GET.get('param')):
        param_uno = request.GET.get('param')
    else:
        param_uno='defecto'
    param_dos = request.GET.get('param2')
    
    context = {'param_uno':param_uno,
                'param_dos':param_dos,
                'hoy':datetime.now(),
                }
    
    return render(request,'wine/index.html',context)

def tintos(request):
    return render(request,'wine/tintos.html')

def blancos(request):
    return render(request,'wine/blancos.html')


def espumantes(request):
    return render(request,'wine/espumantes.html')

def contacto(request):
    return render(request,'wine/contacto.html')

@login_required(login_url='/login/')
def tintos2(request):
    lista_precios = Producto.objects.filter(id_categoria_id__nombre__contains='Tinto')
    return render(request,'wine/tintos2.html', {'precios':lista_precios})

class WineLoginView(LoginView):
    template_name = 'wine/login.html'
    
class WineLogoutView(LogoutView):
    template_name = 'wine/logout.html'