from django.urls import path
from . import views

urlpatterns = [
    # aquivan las url 
    path('', views.calendar_index, name='calendar_index'),
]