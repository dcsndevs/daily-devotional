from django.shortcuts import render, redirect
from django.views import generic
from .forms import RegistrationForm
from django.urls import reverse_lazy

class UserRegistraionView(generic.CreateView):
    form_class = RegistrationForm
    template_name = 'newuser/signup.html'
    success_url = reverse_lazy('account_inactive')
    
    def form_valid(self, form):
        form.instance.is_active = False
        return super().form_valid(form)


def AccountInactiveView(request):
    return render(request, 'newuser/account_inactive.html')
    
