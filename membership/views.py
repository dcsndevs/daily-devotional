from django.shortcuts import render, get_object_or_404, reverse
from django.utils import timezone
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.contrib import messages
from django.http import JsonResponse
from .models import Membership
from .forms import MembershipForm


# Create your views here.
def create_membership(request):
    profile = Membership.objects.filter(status=1)
    if profile:
        return render(request, 'membership/index.html', { 'profile': profile,})
        
        
    else:
        if request.method == 'POST':
            creation_form = MembershipForm(data=request.POST)
            if creation_form.is_valid():
                creation = creation_form.save(commit=False)
                creation.author = request.user
                creation.save()
        
        return render(request, 'membership/create.html', {'creation_form': MembershipForm(),})