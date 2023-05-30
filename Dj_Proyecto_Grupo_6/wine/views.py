from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from datetime import datetime
from .forms import ContactoForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView

## Modelos
from .models import Producto, Precio 

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

def tintos_cards(request):
    return render(request,'wine/tintos_cards.html')

def blancos(request):
    return render(request,'wine/blancos.html')

def espumantes(request):
    return render(request,'wine/espumantes.html')

# def contacto(request):
#     return render(request,'wine/contacto.html')

#Codigo D. revisar que da error ------------------------------------
def contacto(request):
    if request.method == 'POST':
        contacto_form = ContactoForm(request.POST)
        if contacto_form.is_valid():
            contacto_form.save()
            return render(request, 'wine/index.html')
    else:
        contacto_form = ContactoForm()

    return render(request, 'wine/contacto.html', {'form': contacto_form})
#---------------------------------------------

# @login_required(login_url='/login/')
# def tintos2(request):
#     lista_precios = Precio.objects.select_related('id_producto').all()
#     return render(request,'wine/tintos2.html', {'precios':lista_precios})

@login_required(login_url='/login/')
# def login(request):
#     lista_precios = Precio.objects.select_related('id_producto').all()
#     return render(request,'wine/tintos_login.html', {'precios':lista_precios})
def login(request):
    lista_precios = Precio.objects.select_related('id_producto').all()
    return render(request,'wine/tintos_login.html', {'precios':lista_precios})

class WineLoginView(LoginView):
    template_name = 'wine/login.html'
    
class WineLogoutView(LogoutView):
    template_name = 'wine/logout.html'