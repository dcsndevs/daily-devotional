from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import generic
from django.contrib import messages
from .models import Programmes
from .forms import GuestForm, EventRegistrationForm


class PostList(generic.ListView):
    queryset = Programmes.objects.filter(slot=50, status=1)
    template_name = "events/event_list.html"
    paginate_by = 6    


def post_detail(request, slug):
    post = get_object_or_404(Programmes, slug=slug, status=1)
    
    if request.method == "POST":
        form = EventRegistrationForm(request.POST)
        if form.is_valid():
            post_id = post.id
            form.instance.event_id = post_id
            form.instance.author = request.user
            form.save()
            messages.success(
                request,
                'Registration submitted successfully!'
            )
            return redirect(reverse('home'))
    else:
        form = EventRegistrationForm()
    return render(request, 'events/event_detail.html', {"post": post, 'form': form})
    


def current_Programme(request):

    # post = Programmes.objects.all().filter(status=0).first()
    post = Programmes.objects.filter(status=0).order_by('?').first()
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
                
    
    return render(
        request,
        "events/index.html",
        {
            "post": post,
            "guest_form": guest_form,
        },
    )


def event_registration(request):
    if request.method == 'POST':
        form = EventRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registration_success')
    else:
        form = EventRegistrationForm(user=request.user)
    return render(request, 'event_registration.html', {'form': form})