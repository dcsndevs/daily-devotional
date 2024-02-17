from django.urls import path
from . import views


urlpatterns = [

    path('<int:member_id>/', views.post_detail, name='membership'),
    #path('comment/<int:comment_id>/like/', views.like_comment, name='like_comment'),
    #path('<slug:slug>/edit_comment/<int:comment_id>', views.comment_edit, name='comment_edit'),
    #path('<slug:slug>/delete_comment/<int:comment_id>', views.comment_delete, name='comment_delete'),
]
