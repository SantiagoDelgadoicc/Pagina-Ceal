from django.urls import path
from . import views

urlpatterns = [
    # aquivan las url
    path('', views.ceal_index, name='ceal_index'),
]