from django.urls import path, include

from . import views

#CODIGO DE MAURICIO:
urlpatterns = [
    path('', views.index, name='inicio'),
    ##
    path('vinos/<str:parametro>/', views.vinos, name='vinos'),

    ##
    path('espumantes/', views.espumantes, name='espumantes'), 
    path('contacto/', views.contacto, name='contacto'), 
    #path('tintos2/', views.tintos2, name='tintos2'),
    path('login/', views.WineLoginView.as_view(), name='login'), 
    path('logout/', views.WineLogoutView.as_view(), name='logout'), 
]