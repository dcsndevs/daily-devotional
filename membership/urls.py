from django.urls import path
from . import views


urlpatterns = [

    path('create/', views.new_membership, name='new_membership'),
    path('', views.display_membership, name='membership'),
    #path('<slug:owner>/', views.new_membership, name='new_membership'),
    #path('comment/<int:comment_id>/like/', views.like_comment, name='like_comment'),
    #path('<slug:slug>/edit_comment/<int:comment_id>', views.comment_edit, name='comment_edit'),
    #path('<slug:slug>/delete_comment/<int:comment_id>', views.comment_delete, name='comment_delete'),
]
