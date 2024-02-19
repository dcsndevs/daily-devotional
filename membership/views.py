from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.utils import timezone
from django.views.generic import UpdateView, DeleteView
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.utils import timezone
from django.contrib import messages
from django.http import JsonResponse
from django.urls import reverse_lazy
from .models import Membership
from .forms import MembershipForm


# Create your views here.
def display_membership_profile(request):
    profile = Membership.objects.filter(owner=request.user).first()
    print(profile)
    return render(request, 'membership/index.html', { 'profile': profile,})
    
    
def new_membership_profile(request):
    if request.method == "POST":
        creation_form = MembershipForm(request.POST)
        if creation_form.is_valid():
            # Save the form without committing to obtain an instance
            membership = creation_form.save(commit=False)
            # Set the owner ID to the current user ID
            membership.owner_id = request.user.id
            # Save the instance to the database
            membership.save()
            messages.success(request, "You are now a new member!")
            return redirect('view_membership_profile')  # Redirect to the profile page after successful form submission

    else:  # If request method is not POST
        creation_form = MembershipForm()  # Create an empty form

    profile = Membership.objects.filter(owner=request.user)
    return render(request, 'membership/create.html', { 'profile': profile, 'creation_form': creation_form})
    

class update_membership_profile(UpdateView):
    model = Membership
    form_class = MembershipForm
    template_name = 'membership/update.html'
    success_url = reverse_lazy('view_membership_profile')
    
    def form_valid(self, form):
        messages.success(self.request, 'Your Member profile has been successfully updated!')
        return super().form_valid(form)


class delete_membership_profile(DeleteView):
    model = Membership
    template_name = 'membership/delete_member.html'
    success_url = reverse_lazy('membership_delete_success')
    
    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        return response
 
def DeleteSuccessView(request):
    return render(request, 'membership/delete_membership_profile_success.html')