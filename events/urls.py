from django.urls import path
from . import views

urlpatterns = [
    path('schedule', views.PostList.as_view(), name='programe_list'),
    path('<slug:slug>/', views.post_detail, name='programme_detail'),
    path('', views.current_Programme, name='current_programmes'), 
]
