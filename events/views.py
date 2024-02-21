import requests
from django.shortcuts import render, get_object_or_404, reverse
from django.utils import timezone
from django.views import generic, View
from django.http import HttpResponseRedirect, HttpRequest
from django.utils import timezone
from django.contrib import messages
from .models import Programmes



def current_Programme(request):
    post = Programmes.objects.all().filter(status=0).first()
   
    return render(request, 'events/index.html', 
                                {
                                    'post': post,
                                },)