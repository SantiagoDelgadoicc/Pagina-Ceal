from django.urls import include, path
from . import views

urlpatterns = [
    # aquivan las url 
    path('', views.home, name='home'),
    path('ayudas/', include('ayudas.urls')),
]