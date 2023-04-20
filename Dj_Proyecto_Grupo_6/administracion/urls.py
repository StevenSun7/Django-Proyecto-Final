# from django.urls import path

# from . import views

# urlpatterns = [
#     path('', views.index, name='inicio'),
#     path('saludar/<str:nombre>',views.saludar),
# ]

from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('', views.index_administracion,name='inicio_administracion'),
]