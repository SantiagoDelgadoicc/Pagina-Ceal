from django.urls import path
from . import views

urlpatterns = [
    # aquivan las url
    path('', views.computing_index, name='computing_index'),
]