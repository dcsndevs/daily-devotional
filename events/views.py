import requests
from django.shortcuts import render, get_object_or_404, reverse
from django.utils import timezone
from django.views import generic, View
from django.http import HttpResponseRedirect, HttpRequest
from django.utils import timezone
from django.contrib import messages
from .models import Programmes, MemberGuest, Guest
from .forms import GuestForm, MemberGuestForm


class PostList(generic.ListView):
    queryset = Programmes.objects.filter(status=1)
    template_name = "events/event_list.html"


def post_detail(request, slug):
    # post2 = Programmes.objects.all().filter(status=0).first()
    post = get_object_or_404(Programmes, slug=slug, status=1)
    
    if request.method == "POST":
        guest_form = GuestForm(data=request.POST)
        if guest_form.is_valid():
            guest = guest_form.save(commit=False)
            guest.author = request.user
            guest.post = post
            guest.save()
            messages.add_message(
            request, messages.SUCCESS,
            'Resgistration submitted successfully!'
        )
            
    if request.method == "POST":
        guest_form = MemberGuestForm(data=request.POST)
        if guest_form.is_valid():
            guest = guest_form.save(commit=False)
            guest.author = request.user
            guest.post = post
            guest.save()
            messages.add_message(
            request, messages.SUCCESS,
            'Resgistration submitted successfully!'
        )
    
    return render(
        request,
        "events/event_detail.html",
        {
            "post": post,
            "guest_form": guest_registration_form,
            # "member_guest_form": member_guest_form
        },
    )


def current_Programme(request):
    current_date = timezone.now().date()

    # post = Programmes.objects.all().filter(status=0).first()
    post = Programmes.objects.filter(active_date=current_date, status=1).first()
    if request.method == "POST":
        guest_form = GuestForm(data=request.POST)
        if guest_form.is_valid():
            guest = guest_form.save(commit=False)
            guest.author = request.user
            guest.post = post
            guest.save()
            messages.add_message(
            request, messages.SUCCESS,
            'Resgistration submitted successfully!'
        )
            
    if request.method == "POST":
        guest_form = MemberGuestForm(data=request.POST)
        if guest_form.is_valid():
            guest = guest_form.save(commit=False)
            guest.author = request.user
            guest.post = post
            guest.save()
            messages.add_message(
            request, messages.SUCCESS,
            'Resgistration submitted successfully!'
        )
    
    
    return render(
        request,
        "events/index.html",
        {
            "post": post,
            "guest_form": guest_form,
            # "member_guest_form": member_guest_form
        },
    )
