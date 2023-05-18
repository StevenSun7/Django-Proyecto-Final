from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('tintos/', views.tintos, name='tintos'),
    path('blancos/', views.blancos, name='blancos'),
    path('espumantes/', views.espumantes, name='espumantes'), 
    path('contacto/', views.contacto, name='contacto'), 
    path('tintos2/', views.tintos2, name='tintos2'),
    path('accounts/', include('django.contrib.auth.urls')),
    
]