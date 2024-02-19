from django.urls import path
from . import views
from .views import current_date_devotional

urlpatterns = [
    path('', current_date_devotional, name='daily'), 
    path('archive', views.PostList.as_view(), name='archive'),
    path('create/', views.create_post, name='create_post'),
    path('comment/<int:comment_id>/like/', views.like_comment, name='like_comment'),
    path('post/<slug:slug>/like/', views.post_like, name='post_like'),
    # path('view/<str:scripture>/', views.view_bible_reading_plan, name='view_bible_reading_plan'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>', views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>', views.comment_delete, name='comment_delete'),
    path('view/<str:scripture>/', views.view_verse, name='view_verse'),
]
