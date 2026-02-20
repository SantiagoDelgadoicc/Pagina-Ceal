from django.urls import path
from . import views

urlpatterns = [
    # aquivan las url 
    path('', views.projects_index, name='projects_index'),
]