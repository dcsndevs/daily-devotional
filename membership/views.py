from django.shortcuts import render, get_object_or_404, reverse
from django.utils import timezone
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.contrib import messages
from django.http import JsonResponse
from .models import Post, Comment
from .forms import CommentForm


# Create your views here.
