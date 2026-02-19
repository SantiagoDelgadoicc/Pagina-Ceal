from django.urls import path
from . import views

urlpatterns = [
    # aquivan las url 
    path('', views.proyectos_index, name='proyectos_index'),
]