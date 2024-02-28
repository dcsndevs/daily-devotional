from django.urls import path
from . import views

urlpatterns = [
    path('archive', views.PostList.as_view(), name='archive'),
    path('comment/<int:comment_id>/like/', views.like_comment, name='like_comment'),
    path('post/<slug:slug>/like/', views.post_like, name='post_like'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('delete/success/', views.DeleteSuccessView, name='delete_comment_success'),
    path('delete/<int:pk>/', views.DeleteComment.as_view(), name='delete_comment'),
    path('view/<str:scripture>/', views.view_verse, name='view_verse'),
    path('edit/<int:pk>/', views.UpdateComment.as_view(), name='update_comment'),
    path('', views.current_date_devotional, name='daily'), 

]
