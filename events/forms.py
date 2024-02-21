from .models import MemberGuest, Guest
from django import forms

        
class MemberGuestForm(forms.ModelForm):
    class Meta:
        model = MemberGuest
        fields = ('first_name', 'last_name', 'email', 'newsletter')
        
class GuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ('first_name', 'last_name', 'email', 'newsletter')