from .models import HomeContact
from django import forms


class HomeContactForm(forms.ModelForm):
    """
    Form class for visitors to contact site owner
    """
    class Meta:
        model = HomeContact
        fields = ('name', 'subject', 'email', 'message')
