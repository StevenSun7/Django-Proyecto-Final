from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('', views.index_admin, name='index_admin.html'),
    path('lista/', views.lista, name='lista'),
]

