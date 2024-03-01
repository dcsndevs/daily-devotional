from django.contrib.auth import views as auth_views
from django.urls import path
from . import views



urlpatterns = [
    path('change-password/', views.PasswordsChangeView.as_view(template_name='membership/password_change.html'), name='password_change'),
    path('create/', views.new_membership_profile, name='new_membership_profile'),
    path('delete/success/', views.DeleteSuccessView, name='membership_delete_success'),
    path('delete/<int:pk>/', views.delete_membership_profile.as_view(), name='delete_membership_profile'),
    path('edit/<int:pk>/', views.update_membership_profile.as_view(), name='update_membership_profile'),
    path('members/', views.PostList.as_view(), name='community'),
    path('', views.display_membership_profile, name='view_membership_profile'),
    path('<int:owner>/', views.post_detail, name='member_profile'),

]