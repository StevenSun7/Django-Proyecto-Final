from django.urls import path, include, re_path
from . import views

#CODIGO DE MAURICIO:
urlpatterns = [
    path('', views.index, name='inicio'),
    path('vinos/<str:parametro>/', views.vinos, name='vinos'),
    path('tintos/', views.tintos, name='tintos'),
    path('blancos/', views.blancos, name='blancos'),
    path('espumantes/', views.espumantes, name='espumantes'), 
    path('contacto/', views.contacto, name='contacto'), 
    # path('tintos_cards/', views.tintos_cards, name='tintos_cards'),
    path('login/', views.WineLoginView.as_view(), name='login',), 
    path('logout/', views.WineLogoutView.as_view(), name='logout'),
]