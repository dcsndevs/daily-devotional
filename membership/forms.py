from .models import Membership
from django import forms


class MembershipForm(forms.ModelForm):
    class Meta:
        model = Membership
        fields = ['full_name', 'email', 'picture', 'bio', 'location', 'phone',]
        
    def __init__(self, *args, **kwargs):
        self.user_id = kwargs.pop('user_id', None)
        super(MembershipForm, self).__init__(*args, **kwargs)

    def save(self, commit=True, user_id=None):
        instance = super(MembershipForm, self).save(commit=False)
        if user_id:
            instance.owner_id = user_id
        if commit:
            instance.save()
        return instance
    
    widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'picture': forms.FileInput(attrs={'class': 'form-control-file'}),
            'bio': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'type': 'number', 'pattern': '[0-9]*'}),
        }
    
