from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from datetime import datetime
from .forms import ContactoForm
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


@login_required(login_url='/login/')
def vinos(request, parametro):
    
    filtro = 'tinto'
    if parametro =='blanco' :
        filtro = 'blanco'
    
    lista_precios = Producto.objects.filter(id_categoria_id__agrupado=filtro).order_by('id_producto')[:20]
    
    if parametro == 'blanco':
        return render(request,'wine/blancos.html', {'precios':lista_precios})
    else:
        return render(request,'wine/tintos.html', {'precios':lista_precios})


def espumantes(request):
    return render(request,'wine/espumantes.html')


def contacto(request):
    if request.method == 'POST':
        contacto_form = ContactoForm(request.POST)
        if contacto_form.is_valid():
            contacto_form.save()
            return render(request, 'wine/index.html')
    else:
        contacto_form = ContactoForm()

    return render(request, 'wine/contacto.html', {'form': contacto_form})


class WineLoginView(LoginView):
    template_name = 'wine/login.html'
    
class WineLogoutView(LogoutView):
    template_name = 'wine/logout.html'