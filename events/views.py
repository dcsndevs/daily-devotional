from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic import ListView, DetailView
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Event

class EventList(ListView):
    
    queryset = Event.objects.filter(status=1)
    template_name = "events/index.html"
    paginate_by = 6
   

class EventDetail(DetailView):
    model = Event
    template_name = 'events/event_detail.html'
    context_object_name = 'post'
    slug_url_kwarg = 'slug'


def EventDetail2(request, slug):
    post = get_object_or_404(Event, slug=slug)
    return render(request, 'events/event_detail.html', {'post': post})