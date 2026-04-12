from django.urls import path
from . import views

urlpatterns = [
    path('', views.assistance_index, name='assistance_index'),
    path('crear-solicitud/', views.crear_solicitud, name='crear_solicitud'),
]
