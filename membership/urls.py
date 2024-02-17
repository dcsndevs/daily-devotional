from django.urls import path
from . import views


urlpatterns = [
    path('create/', views.new_membership, name='new_membership'),
    path('', views.display_membership, name='membership'),
    path('edit/', views.edit_membership, name='edit_membership'),
    path('<slug:slug>/edit_profile/<int:owner_id>', views.edit_profile, name='edit_profile'),
    path('<slug:slug>/delete_profile/<int:owner_id>', views.delete_profile, name='delete_profile'),
]
