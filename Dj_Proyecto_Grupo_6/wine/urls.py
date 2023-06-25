from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('vinos/<str:parametro>/', views.vinos, name='vinos'),
    path('espumantes/', views.espumantes, name='espumantes'), 
    path('contacto/', views.contacto, name='contacto'),
    path('login/', views.WineLoginView.as_view(), name='login'), 
    path('logout/', views.WineLogoutView.as_view(), name='logout'), 
]