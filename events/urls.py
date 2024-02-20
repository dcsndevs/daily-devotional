from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='all_events'),
    path('<slug:slug>/', views.post_detail, name='event_detail'),

]
