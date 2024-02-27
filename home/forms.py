from .models import HomeContact
from django import forms

        
class HomeContactForm(forms.ModelForm):
    class Meta:
        model = HomeContact
        fields = ('name', 'subject', 'email', 'message')