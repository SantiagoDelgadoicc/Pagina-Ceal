from django.urls import path
from . import views

urlpatterns = [
    # aquivan las url
    path('', views.resources_index, name='resources_index'),
]