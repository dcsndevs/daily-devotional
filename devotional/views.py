from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views import generic
from django.views.generic import DetailView
from django.utils import timezone
from .models import Post


# def post_list(request):
#     posts = Post.objects.filter(status=1)
#     return render(request, 'devotional/post_list.html', {'posts': posts})

class PostList(generic.ListView):
    current_date = timezone.now().date()
    # queryset = Post.objects.filter(active_date__lt=current_date)
    queryset = Post.objects.filter()
    template_name = "devotional/archive.html"


def post_detail(request, slug):
    current_date = timezone.now().date()
    post = get_object_or_404(Post, slug=slug, status=1)
    return render(request, 'devotional/post_detail.html', {'post': post})


def current_date_devotional(request):
    # Retrieve the current date
    current_date = timezone.now().date()
    # Retrieve the post with the current date
    post = Post.objects.filter(active_date=current_date, status=1).first()
    return render(request, 'devotional/index.html', {'post': post})