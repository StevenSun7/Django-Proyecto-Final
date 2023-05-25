from django.urls import path, include
from . import views

#CODIGO DE MAURICIO:
urlpatterns = [
    path('', views.index, name='inicio'),
    path('tintos/', views.tintos, name='tintos'),
    path('blancos/', views.blancos, name='blancos'),
    path('espumantes/', views.espumantes, name='espumantes'), 
    path('contacto/', views.contacto, name='contacto'), 
    # path('tintos_login/', views.tintos_login, name='tintos_login'),
    path('login/', views.WineLoginView.as_view(), name='login',), 
    path('logout/', views.WineLogoutView.as_view(), name='logout'), 
]