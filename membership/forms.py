from .models import Membership
from django import forms


class MembershipForm(forms.ModelForm):
    class Meta:
        model = Membership
        fields = ('full_name', 'email', 'picture', 'bio', 'location', 'phone',)
        
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