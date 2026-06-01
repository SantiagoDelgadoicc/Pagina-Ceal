from django.urls import path
from . import views

urlpatterns = [
    path('', views.calendar_index, name='calendar_index'),
    path('create/', views.create_event, name='create_event'),
    path('update/<int:event_id>/', views.update_event, name='update_event'),
]