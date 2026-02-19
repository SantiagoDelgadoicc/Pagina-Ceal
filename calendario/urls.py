from django.urls import path
from . import views

urlpatterns = [
    # aquivan las url 
    path('', views.calendario_index, name='calendario_index'),
]