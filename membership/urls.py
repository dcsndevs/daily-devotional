from django.urls import path
from . import views


urlpatterns = [
    path('', views.display_membership_profile, name='membership'),
    path('create/', views.new_membership_profile, name='new_membership_profile'),
    path('edit/<int:pk>/', views.update_membership_profile.as_view(), name='update_membership_profile'),
    path('delete/<int:pk>/', views.delete_membership_profile.as_view(), name='delete_membership_profile'),
]
