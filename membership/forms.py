from .models import Membership
from django import forms


class MembershipForm(forms.ModelForm):
    class Meta:
        model = Membership
        fields = ('full_name', 'email', 'picture', 'bio', 'location', 'phone',)