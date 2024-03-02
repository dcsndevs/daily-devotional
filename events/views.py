from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import generic
from django.contrib import messages
from .models import Programmes, Attendee
from .forms import EventRegistrationForm


class PostList(generic.ListView):
    """
    View for displaying a list of event posts.
    This view retrieves a list of active event posts and displays them in a
    paginated manner.
    It fetches the events from the database using the `Post` model.
    **Context**

    ``queryset``
        All published instances of :model:`event.Programmes`
    ``paginate_by``
        Number of posts per page.
    **Template:**

    :template:`events/event_list.html`
    """

    queryset = Programmes.objects.filter(status=1)
    template_name = "events/event_list.html"
    paginate_by = 6


def post_detail(request, slug):
    """
    View for displaying the details of a specific event post.
    This view retrieves a specific event post identified by its slug from the
    database using the `Post` model.
    It also retrieves the associated comments for the post.
    **Context**

    ``post``
        An instance of :model:`event.Programmes`.
    ``EventRegistrationForm``
        An instance of :form:`event.EventRegistrationForm

    **Template:**

    :template:`events/event_detail.html`
    """

    post = get_object_or_404(Programmes, slug=slug, status=1)
    slot = post.slot
    used_slot = Attendee.objects.filter(event=post.id).count()
    email_per_event = Attendee.objects.filter(event=post.id)
    remaining_slot = slot - used_slot

    if remaining_slot == 0:
        return render(request, 'events/event_detail.html',
                      {'post': post, 'remaining_slot': remaining_slot})

    elif request.method == "POST":
        form = EventRegistrationForm(request.POST)
        email = request.POST.get('email')
        if form.is_valid():
            # Check if the event is fully booked
            if remaining_slot == 0:
                messages.warning(request,
                                 'Sorry this programme is fully booked!')
                return render(request, 'events/event_detail.html',
                              {'post': post})
            # Check if the email is already registered for this event
            elif email not in email_per_event:
                messages.warning(request,
                                 'Sorry this email has already been'
                                 'registered before!')
                return render(request, 'events/event_detail.html',
                              {'post': post, 'form': form,
                               'remaining_slot': remaining_slot})
            else:
                post_id = post.id
                form.instance.event_id = post_id
                form.save()
                messages.success(request,
                                 'Registration submitted successfully!')
                return redirect(reverse('home'))
    else:
        form = EventRegistrationForm(user=request.user)
    return render(request, 'events/event_detail.html',
                  {'post': post, 'form': form,
                   'remaining_slot': remaining_slot})


def current_Programme(request):
    """
    View for displaying the details of a specific event post.
    This view retrieves a specific event post identified by its slug from the
    database using the `Post` model.
    It also retrieves the associated comments for the post.
    **Context**

    ``post``
        An instance of :model:`event.Programmes`.
    ``EventRegistrationForm``
        An instance of :form:`event.EventRegistrationForm

    **Template:**

    :template:`events/event_detail.html`
    """

    post = Programmes.objects.filter(status=1).order_by('?').first()
    slot = post.slot
    used_slot = Attendee.objects.filter(event=post.id).count()
    email_per_event = Attendee.objects.filter(event=post.id)
    remaining_slot = slot - used_slot

    if remaining_slot == 0:
        return render(request, 'events/index.html',
                      {'post': post, 'remaining_slot': remaining_slot})

    elif request.method == "POST":
        form = EventRegistrationForm(request.POST)
        email = request.POST.get('email')
        text = 'Sorry this email has already been registered for this event!'
        if form.is_valid():
            # Check if the event is fully booked
            if remaining_slot == 0:
                messages.warning(request,
                                 'Sorry this programme is fully booked!')
                return render(request, 'events/index.html', {'post': post})
            # Check if the email is already registered for this event
            elif email not in email_per_event:
                messages.warning(request, text)
                return render(request, 'events/index.html',
                              {'post': post,
                               'form': form,
                               'remaining_slot': remaining_slot})
            else:
                post_id = post.id
                form.instance.event_id = post_id
                form.save()
                messages.success(request,
                                 'Registration submitted successfully!')
                return redirect(reverse('home'))
    else:
        form = EventRegistrationForm(user=request.user)
    return render(request, 'events/index.html',
                           {'post': post, 'form': form,
                            'remaining_slot': remaining_slot})
