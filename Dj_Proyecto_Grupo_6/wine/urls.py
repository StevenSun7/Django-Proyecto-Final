from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('tintos/', views.tintos, name='tintos'),
    path('blancos/', views.blancos, name='blancos'),
    path('espumantes/', views.espumantes, name='espumantes'), 
    path('contacto/', views.contacto, name='contacto'), 
    path('tintos2/', views.tintos2, name='tintos2'),
    path('logout/', views.logout_vw, name='logout_vw'),
    path('accounts/login/', views.CustomLoginView.as_view(),  name = 'login'),
    path('login/', views.login_process,  name = 'login_process'),
]