from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from datetime import datetime
# Create your views here.
def index(request):
    if(request.GET.get('param')):
        param_uno = request.GET.get('param')
    else:
        param_uno='defecto'
    param_dos = request.GET.get('param2')
    #return HttpResponse(f"""
     #    <h1>Proyecto Django - Codo a Codo🦄</h1>""")
    listado_cursos = [
        {
            'nombre':'Fullstack Java',
            'descripcion':'Curso de Fullstack',
            'categoria':'Programación',
        },
        {
            'nombre':'Diseño UX/UI',
            'descripcion':'🖌🎨',
            'categoria':'Diseño',
        },
        {
            'nombre':'Big Data',
            'descripcion':'test',
            'categoria':'Análisis de Datos',
        },
        {
            'nombre':'Big Data Avanzado',
            'descripcion':'test',
            'categoria':'Análisis de Datos Avanzado',
        },
    ]
    context = {'param_uno':param_uno,
                  'param_dos':param_dos,
                  'param_tres':'hola',
                  'hoy':datetime.now(),
                  'cursos':listado_cursos,
                  }

    return render(request,'publica/index.html',context)

def tintos(request):
    return render(request,'publica/tintos.html')

def blancos(request):
    return render(request,'publica/blancos.html')

def espumantes(request):
    return render(request,'publica/espumantes.html')

def contacto(request):
    return render(request,'publica/contacto.html')

def quienes_somos(request):
    template = loader.get_template('publica/quienes_somos.html')
    context = {'titulo': 'Quienes somos'}
    return HttpResponse(template.render(context,request))
    #return render(request,'publica/quienes_somos.html')
    #return HttpResponse(f"""
    #    <h1>Proyecto Django - Quienes somos</h1>""")


def saludar (request,nombre):
    if(request.method=='GET'):
        return HttpResponse(f"""
            <h1>ENTRE POR GET - {nombre}</h1>
        """)
    else:
        return HttpResponse(f"""
            <h1>Hola Django - {nombre}</h1>
        """)

def ver_proyectos(request,anio,mes):
    return HttpResponse(f"""
         <h1>Proyectos del {mes}/{anio}</h1>""")

def ver_proyectos_2023_04(request):        
    return HttpResponse(f"""
            <h1>Proyectos del mes de Abril 2023</h1>
        """)


