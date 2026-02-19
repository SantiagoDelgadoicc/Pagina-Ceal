from django.urls import path
from . import views

urlpatterns = [
    # aquivan las url
    path('', views.ayudas_index, name='ayudas_index'),
]