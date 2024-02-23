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
    email_per_event = Attendee.objects.filter(event=post.id)
    remaining_slot = slot - used_slot
    
    if remaining_slot == 0:
        
        return render(request, 'events/event_detail.html', {'post': post, 'remaining_slot': remaining_slot})
    
    elif request.method == "POST":
        
        form = EventRegistrationForm(request.POST)
        email = request.POST.get('email')
        if form.is_valid():
            #to double check just incase a user has access to the form before slot finished
            if remaining_slot == 0:
                messages.warning(
                    request,
                    'Sorry this programme is fully booked!'
                )
                return render(request, 'events/event_detail.html', {'post': post})
            elif email not in email_per_event:
                messages.warning(
                    request,
                    'Sorry this email has already been registered for this event!'
                )
                return render(request, 'events/event_detail.html', {'post': post, 'form': form, 'remaining_slot': remaining_slot})
                
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
        form = EventRegistrationForm(user=request.user)
    return render(request, 'events/event_detail.html', {'post': post, 'form': form, 'remaining_slot': remaining_slot})
    

def current_Programme(request):
    
    post = Programmes.objects.filter(status=1).order_by('?').first()
    print(post.slot)
    slot = post.slot
    used_slot = Attendee.objects.filter(event=post.id).count()
    email_per_event = Attendee.objects.filter(event=post.id)
    remaining_slot = slot - used_slot
    
    if remaining_slot == 0:
        
        return render(request, 'events/index.html', {'post': post, 'remaining_slot': remaining_slot})
    
    elif request.method == "POST":
        
        form = EventRegistrationForm(request.POST)
        email = request.POST.get('email')
        if form.is_valid():
            #to double check just incase a user has access to the form before slot finished
            if remaining_slot == 0:
                messages.warning(
                    request,
                    'Sorry this programme is fully booked!'
                )
                return render(request, 'events/index.html', {'post': post})
            elif email not in email_per_event:
                messages.warning(
                    request,
                    'Sorry this email has already been registered for this event!'
                )
                return render(request, 'events/index.html', {'post': post, 'form': form, 'remaining_slot': remaining_slot})
                
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
        form = EventRegistrationForm(user=request.user)
    return render(request, 'events/index.html', {'post': post, 'form': form, 'remaining_slot': remaining_slot})
 