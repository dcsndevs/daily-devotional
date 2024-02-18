from django.shortcuts import render, get_object_or_404, reverse
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
    if profile:
        return render(request, 'membership/index.html', { 'profile': profile,})
        
        
    else:
        # if request.method == 'POST':
        #     creation_form = MembershipForm(data=request.POST)
        #     if creation_form.is_valid():
        #         creation = creation_form.save(commit=False)
        #         creation.author = request.user
        #         creation.save()
        
        return render(request, 'membership/create.html', {'creation_form': MembershipForm(user_id=request.user.id),})
    
    
def new_membership_profile(request):
    if request.method == "POST":
        creation_form = MembershipForm(request.POST, user_id=request.user.id)
        if creation_form.is_valid():
            creation_form.save(user_id=request.user.id)
            messages.add_message(request, messages.SUCCESS, "You are now a new member!")

    creation_form = MembershipForm(user_id=request.user.id)
    profile = Membership.objects.filter(status=1).first()
    return render(request, 'membership/create.html', { 'profile': profile, 'creation_form': creation_form,})
    
# def edit_membership(request):
#     profile = Membership.objects.filter(wner_id=request.user.id).first()
#     edit_form = MembershipForm(user_id=request.user.id)
#     return render(request, 'membership/edit.html', { 'profile': profile, 'edit_form': edit_form,})


# def edit_profile(request, id, owner_id):

#     if request.method == "POST":
#         queryset = Membership.objects.filter(owner_id=request.user.id)
#         post = get_object_or_404(queryset, id=id)
#         profile = get_object_or_404(Membership, pk=owner_id)
#         membership_form = MembershipForm(data=request.POST, instance=profile)

#         if membership_form.is_valid() and profile.user == request.user:
#             profile = membership_form.save(commit=False)
#             profile.post = post
#             profile.save()
#             messages.add_message(request, messages.SUCCESS, 'Profile Update is successfully!')
#         else:
#             messages.add_message(request, messages.ERROR, 'Error: Could not update Profile!')

#     return HttpResponseRedirect(reverse('edit_membership', args=[id]))


# def delete_profile(request, id, owner_id):
#     """
#     view to delete profile
#     """
#     queryset = Membership.objects.filter(wner_id=request.user.id)
#     post = get_object_or_404(queryset, id=id)
#     profile = get_object_or_404(Membership, pk=owner_id)

#     if profile.user == request.user:
#         profile.delete()
#         messages.add_message(request, messages.SUCCESS, 'Profile deleted!')
#     else:
#         messages.add_message(request, messages.ERROR, 'You can only delete your own profile!')

#     return HttpResponseRedirect(reverse('membership', args=[id]))


class update_membership_profile(UpdateView):
    model = Membership
    form_class = MembershipForm
    template_name = 'membership/update.html'
    success_url = reverse_lazy('membership')
    
    def form_valid(self, form):
        messages.success(self.request, 'Your Member profile has been successfully updated!')
        return super().form_valid(form)


class delete_membership_profile(DeleteView):
    model = Membership
    template_name = 'membership/delete_member.html'
    success_url = reverse_lazy('membership')
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Your Member profile has been successfully deleted!')
        return super().delete(request, *args, **kwargs)
 