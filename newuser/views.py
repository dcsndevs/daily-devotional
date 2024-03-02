from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from .forms import RegistrationForm


class UserRegistraionView(generic.CreateView):
    """
    View for displaying a new user registration form
    This view retrieves a list of active blog posts and displays them in a
    paginated manner.
    It fetches the posts from the database using the `Post` model.
    **Context**

    ``queryset``
        Instances of django auyth framework :model:`.auth`
    **Template:**

    :template:`newuser/signup.html`
    """
    form_class = RegistrationForm
    template_name = 'newuser/signup.html'
    success_url = reverse_lazy('account_inactive')

    def form_valid(self, form):
        form.instance.is_active = False
        return super().form_valid(form)


def AccountInactiveView(request):
    """
    View for displaying info about newly registered users being inactive
    **Template:**

    :template:`newuser/account_inactive.html`
    """
    return render(request, 'newuser/account_inactive.html')
