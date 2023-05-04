from django.urls import path

from . import views

urlpatterns = [    
    path('', views.index, name='inicio'),

    path('tintos/', views.tintos, name='tintos'),
    path('blancos/', views.blancos, name='blancos'),
    path('espumantes/', views.espumantes, name='espumantes'), 
    path('contacto/', views.contacto, name='contacto'), 

    path('quienes_somos/', views.quienes_somos, name='quienes_somos'),
    path('saludar/<str:nombre>/',views.saludar, name='saludar'),

    path('proyectos/<int:anio>/<int:mes>',views.ver_proyectos, name='ver_proeyctos'),
    path('proyectos/2023/04/',views.ver_proyectos_2023_04,name='ver_proyectos_23_04'),
    path('proyectos/<int:anio>/',views.ver_proyectos,name='ver_proyectos_defecto'),
 ]