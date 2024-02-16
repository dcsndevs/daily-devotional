from django.urls import path
from . import views
from .views import current_date_devotional

urlpatterns = [
    path('archive', views.PostList.as_view(), name='archive'),
    # path('', views.post_list, name='post_list'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('', current_date_devotional, name='daily'),  # Add this line for the PostDetailView
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]
