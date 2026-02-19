from django.urls import path
from . import views

urlpatterns = [
    # aquivan las url
    path('', views.dashboard_index, name='dashboard_index'),
]