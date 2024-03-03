from django.contrib.auth import views as auth_views
from django.urls import path
from . import views



urlpatterns = [
    path('change-password/', views.PasswordsChangeView.as_view(template_name='persona/password_change.html'), name='password_change'),
    path('create/', views.new_persona_profile, name='new_persona_profile'),
    path('delete/success/', views.DeleteSuccessView, name='persona_delete_success'),
    path('delete/<int:pk>/', views.delete_persona_profile.as_view(), name='delete_persona_profile'),
    path('edit/<int:pk>/', views.update_Persona_profile.as_view(), name='update_Persona_profile'),
    path('members/', views.PostList.as_view(), name='community'),
    path('', views.display_Persona_profile, name='view_Persona_profile'),
    path('<int:owner>/', views.post_detail, name='member_profile'),

]