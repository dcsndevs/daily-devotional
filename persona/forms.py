from .models import Persona
from django import forms


class PersonaForm(forms.ModelForm):
    """
    Form class for users to register their profiles
    """
    class Meta:
        model = Persona
        fields = ['first_name', 'last_name', 'email', 'picture', 'bio',
                                'location', 'where_from', 'phone',
                  'relationship_status', 'favourite_scripture',
                  'favourite_bible_character', 'education', 'handle']

    def __init__(self, *args, **kwargs):
        self.user_id = kwargs.pop('user_id', None)
        self.user = kwargs.pop('user', None)
        super(PersonaForm, self).__init__(*args, **kwargs)

        if self.user and self.user.is_authenticated:
            self.fields['first_name'].initial = self.user.first_name
            self.fields['last_name'].initial = self.user.last_name
            self.fields['email'].initial = self.user.email

    def save(self, commit=True, user_id=None):
        instance = super(PersonaForm, self).save(commit=False)
        if user_id:
            instance.owner_id = user_id
        if commit:
            instance.save()
        return instance
