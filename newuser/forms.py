from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#To make the email field compulsory in user registration
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if not email:
            raise forms.ValidationError("Email field is required.")
        return email