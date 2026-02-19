from django.urls import path
from . import views

urlpatterns = [
    # aquivan las url
    path('', views.carrera_index, name='carrera_index'),
]