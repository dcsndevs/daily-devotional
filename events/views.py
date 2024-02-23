from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import generic
from django.contrib import messages
from .models import Programmes, Attendee
from .forms import GuestForm, EventRegistrationForm


class PostList(generic.ListView):
    queryset = Programmes.objects.filter(status=1)
    template_name = "events/event_list.html"
    paginate_by = 6    


def post_detail(request, slug):
    post = get_object_or_404(Programmes, slug=slug, status=1)
    slot = post.slot
    used_slot = Attendee.objects.filter(event=post.id).count()
    print(used_slot)
    remaining_slot = slot - used_slot
    
    if remaining_slot == 0:
        
        return render(request, 'events/event_detail.html', {'post': post, 'remaining_slot': remaining_slot})
    
    elif request.method == "POST":
        
        form = EventRegistrationForm(request.POST)
        if form.is_valid():
            if remaining_slot == 0:
                messages.success(
                    request,
                    'Sorry this programme is fully booked!'
                )
                return render(request, 'events/event_detail.html', {'post': post})
            else:
                post_id = post.id
                form.instance.event_id = post_id
                form.save()
                messages.success(
                    request,
                    'Registration submitted successfully!'
                )
                return redirect(reverse('home'))
    else:
        form = EventRegistrationForm()
    return render(request, 'events/event_detail.html', {'post': post, 'form': form, 'remaining_slot': remaining_slot})
    


def current_Programme(request):
    #this view should inherit from post_detail; the difference is the filter option that specifies which to show
    # post = Programmes.objects.all().filter(status=0).first()
    post = Programmes.objects.filter(status=0).order_by('?').first()
    
    
    return render(
        request,
        "events/index.html",
        {
            'post': post,
            #'form': form,
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