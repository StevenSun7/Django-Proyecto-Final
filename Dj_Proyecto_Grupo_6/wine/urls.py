from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('saludar/<str:nombre>',views.index),
]