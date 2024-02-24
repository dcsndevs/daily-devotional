import cloudinary.uploader
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.db import transaction
from django.utils import timezone
from django.views.generic import UpdateView, DeleteView
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.urls import reverse_lazy
from .models import Profile
from .forms import ProfileForm
from cloudinary.uploader import upload

@login_required
def display_membership_profile(request):
    profile = Profile.objects.filter(owner=request.user).first()
    return render(request, 'membership/index.html', { 'profile': profile,})
    
    
@login_required
def new_membership_profile(request):
    if request.method == "POST":
        creation_form = ProfileForm(request.POST, request.FILES)
        if creation_form.is_valid():
            membership = creation_form.save(commit=False)
            membership.owner = request.user  # Set the owner to the current user

            # Check if a picture was uploaded
            if 'picture' in request.FILES:
                image_file = request.FILES['picture']
                result = cloudinary.uploader.upload(image_file)
                membership.picture = result['secure_url']
            else:
                # Provide a default placeholder image URL
                membership.picture = 'static/images/default.jpg'

            # Save the membership and related user
            with transaction.atomic():
                membership.save()
                # Also update the User record in Auth
                request.user.first_name = creation_form.cleaned_data['first_name']
                request.user.last_name = creation_form.cleaned_data['last_name']
                request.user.email = creation_form.cleaned_data['email']
                request.user.save()

            messages.success(request, "You are now a new member!")
            return redirect('view_membership_profile')
    else:
        creation_form = ProfileForm(user=request.user)
    return render(request, 'membership/create.html', {'creation_form': creation_form})


class update_membership_profile(UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'membership/update.html'
    success_url = reverse_lazy('view_membership_profile')
    
    def form_valid(self, form):
        messages.success(self.request, 'Your Member profile has been successfully updated!')
        return super().form_valid(form)


class delete_membership_profile(DeleteView):
    model = Profile
    template_name = 'membership/delete_member.html'
    success_url = reverse_lazy('membership_delete_success')
    
    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        return response
 
def DeleteSuccessView(request):
    return render(request, 'membership/delete_membership_profile_success.html')