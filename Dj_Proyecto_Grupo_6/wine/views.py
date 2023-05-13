from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.views import LoginView

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

def blancos(request):
    return render(request,'wine/blancos.html')

def espumantes(request):
    return render(request,'wine/espumantes.html')

def contacto(request):
    return render(request,'wine/contacto.html')

@login_required
def tintos2(request):
    print('testatasgasfasdfsdfsds')
    lista_precios = Precio.objects.select_related('id_producto').all()
    
    return render(request,'wine/tintos2.html', {'precios':lista_precios})


def logout_vw(request):
    logout(request)
    
class CustomLoginView(LoginView):
    template_name = 'wine/login.html'
    print('sdfasdfasdf')


def login_process(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            print( "ok ")
            return redirect('/')
        else:
            # Mostrar mensaje de error si las credenciales son incorrectas
            error_message = "Invalid username or password"
            print(error_message)
            return render(request, 'login.html', {'error_message': error_message})

    return render(request, 'login.html')