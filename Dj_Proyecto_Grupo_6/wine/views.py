from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from wine.forms import ContactoForm
from datetime import datetime

# Create your views here.
def index(request):
    mensaje=None
    if(request.method=='POST'):
        contacto_form = ContactoForm(request.POST)
        mensaje='Hemos recibido tus datos'
        #accion para tomar los datos del formulario
    else:
        contacto_form = ContactoForm()
    listado_cursos = [
       {
           'nombre':'Coaching digital',
       }
    
    ]

#    if(request.GET.get('param')):
#        param_uno = request.GET.get('param')
#    else:
#        param_uno='defecto'
#    param_dos = request.GET.get('param2')
    
    context = { 'cursos':listado_cursos,
               'mensaje':mensaje,
               'contacto_form':contacto_form,
        'hoy':datetime.now(),}
    
    return render(request,'wine/index.html',context)

def tintos(request):
    return render(request,'wine/tintos.html')

def blancos(request):
    return render(request,'wine/blancos.html')

def espumantes(request):
    return render(request,'wine/espumantes.html')

def contacto(request):
    return render(request,'wine/contacto.html')
