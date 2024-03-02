from django.urls import path
from .views import UserRegistraionView, AccountInactiveView


urlpatterns = [
    path('account_inactive/', AccountInactiveView, name='account_inactive'),
    path('registration/',
         UserRegistraionView.as_view(template_name='newuser/signup.html'),
         name='registration'),

]
