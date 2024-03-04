import cloudinary.uploader
from django.shortcuts import render, get_object_or_404, redirect
from django.db import transaction
from django.views import generic
from django.views.generic import UpdateView, DeleteView
from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .models import Profile
from .forms import ProfileForm


class PostList(generic.ListView):
    """
    View for displaying a member profile details.
    This view retrieves a list of active profiles and displays them in a
    paginated manner.
    It fetches the posts from the database using the `Post` model.
    **Context**

    ``queryset``
        All published instances of :model:`membership.Profile`
    ``paginate_by``
        12 profiles per page.
    **Template:**

    :template:`membership/community.html`
    """
    queryset = Profile.objects.filter(status=1)
    template_name = "membership/community.html"
    paginate_by = 12


@login_required
def display_membership_profile(request):
    """
    View for displaying a detailed profile of members.
    It fetches the posts from the database using the `Post` model.
    **Context**

    ``queryset``
        All published instances of :model:`membership.Profile`
    **Template:**

    :template:`membership/index.html`
    """
    profile = Profile.objects.filter(owner=request.user).first()
    return render(request, 'membership/index.html', {'profile': profile, })


@login_required
def new_membership_profile(request):
    """
    View for displaying a member profile details.
    This view retrieves existig infor and allows for editing.
    It fetches the posts from the database using the `Post` model.
    **Context**

    ``queryset``
        All published instances of :model:`membership.Profile`
    **Template:**

    :template:`membership/create.html`
    """
    if request.method == "POST":
        creation_form = ProfileForm(request.POST, request.FILES)
        if creation_form.is_valid():
            membership = creation_form.save(commit=False)
            membership.owner = request.user

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
                anchor = request.user
                # Also update the User record in Auth
                anchor.first_name = creation_form.cleaned_data['first_name']
                anchor.last_name = creation_form.cleaned_data['last_name']
                anchor.email = creation_form.cleaned_data['email']
                anchor.save()

            messages.success(request, "You are now a new member!")
            return redirect('view_membership_profile')
    else:
        creation_form = ProfileForm(user=request.user)
    return render(request, 'membership/create.html',
                  {'creation_form': creation_form})


def post_detail(request, owner):
    """
    View for displaying a selected member profile details.
    This view retrieves existig infor and allows for editing.
    It fetches the posts from the database using the `Post` model.
    **Context**

    ``queryset``
        All published instances of :model:`membership.Profile`
    **Template:**

    :template:`membership/slected-member-profile-detail.html`
    """

    profile = get_object_or_404(Profile, owner=owner, status=1)

    return render(
        request,
        "membership/slected-member-profile-detail.html",
        {
            "profile": profile,
        },
    )


class update_membership_profile(UpdateView):
    """
    View for editing profile details.
    **Context**

    ``queryset``
        All published instances of :model:`membership.Profile`
    **Template:**

    :template:`membership/update.html`
    """

    model = Profile
    form_class = ProfileForm
    template_name = 'membership/update.html'
    success_url = reverse_lazy('view_membership_profile')

    def form_valid(self, form):
        messages.success(self.request,
                         'Your Member profile has been successfully updated!')
        return super().form_valid(form)


class delete_membership_profile(DeleteView):
    """
    View for deleting profile details.
    **Context**
    ``queryset``
        All published instances of :model:`membership.Profile`
    **Template:**
    :template:`membership/delete_member.html`
    """
    model = Profile
    template_name = 'membership/delete_member.html'
    success_url = reverse_lazy('membership_delete_success')

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        return response


def DeleteSuccessView(request):
    """
    View for confirming deleted profile details.
    **Context**
    ``queryset``
        All published instances of :model:`membership.Profile`
    **Template:**
    :template:`membership/delete_membership_profile_success.html`
    """
    return render(request, 'membership/delete_membership_profile_success.html')


class PasswordsChangeView(PasswordChangeView):
    """
    View for changin profile member passord.
    **Context**
    """

    form_class = PasswordChangeForm
    success_url = reverse_lazy('view_membership_profile')

    def form_valid(self, form):
        messages.success(self.request,
                         'Your Password has been successfully updated!')
        return super().form_valid(form)
