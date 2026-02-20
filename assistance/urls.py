from django.urls import path
from . import views

urlpatterns = [
    # aquivan las url
    path('', views.assistance_index, name='assistance_index'),
]