from allauth.account.adapter import DefaultAccountAdapter

#We write this to overide the dault and subject intending users to be approved before having access
class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        user = super().save_user(request, user, form, commit=False)
        user.is_active = False  # Set the user to inactive by default
        if commit:
            user.save()
        return user