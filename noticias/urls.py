from django.urls import path
from . import views

urlpatterns = [
    # aquivan las url
    path('', views.noticias_index, name='noticias_index'),
]