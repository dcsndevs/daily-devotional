from .models import Attendee, Programmes
from django import forms


class EventRegistrationForm(forms.ModelForm):
    """
    Form class for users to register for an event
    """

    class Meta:
        model = Attendee
        exclude = ['event']
        fields = ['first_name', 'last_name', 'email', 'newsletter']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(EventRegistrationForm, self).__init__(*args, **kwargs)

        if self.user and self.user.is_authenticated:
            self.fields['first_name'].initial = self.user.first_name
            self.fields['last_name'].initial = self.user.last_name
            self.fields['email'].initial = self.user.email
