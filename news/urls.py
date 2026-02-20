from django.urls import path
from . import views

urlpatterns = [
    # aquivan las url
    path('', views.news_index, name='news_index'),
]