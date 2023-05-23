from django.urls import path
from . import views

#CODIGO QUE TENIAMOS:
# urlpatterns = [
#     path('', views.index, name='inicio'),
#     path('tintos/', views.tintos, name='tintos'),
#     path('blancos/', views.blancos, name='blancos'),
#     path('espumantes/', views.espumantes, name='espumantes'), 
#     path('contacto/', views.contacto, name='contacto'), 
#     path('login/', views.login, name='login'), 
# ]

#CODIGO DE MAURICIO:
urlpatterns = [
    path('', views.index, name='inicio'),
    path('tintos/', views.tintos, name='tintos'),
    path('blancos/', views.blancos, name='blancos'),
    path('espumantes/', views.espumantes, name='espumantes'), 
    path('contacto/', views.contacto, name='contacto'), 
    path('tintos2/', views.tintos2, name='tintos2'),
    path('login/', views.WineLoginView.as_view(), name='login'), 
    path('logout/', views.WineLogoutView.as_view(), name='logout'), 
]