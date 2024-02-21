from django.urls import path
from . import views

urlpatterns = [

    path('', views.current_Programme, name='programmes'), 
]