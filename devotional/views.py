from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views import generic
from django.views.generic import DetailView
from django.utils import timezone
from django.contrib import messages
from .models import Post
from .forms import CommentForm


class PostList(generic.ListView):
    current_date = timezone.now().date()
    queryset = Post.objects.filter()
    template_name = "devotional/archive.html"


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, status=1)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()
    
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
            request, messages.SUCCESS,
            'Comment submitted successfully!'
        )
    
    comment_form = CommentForm()

    return render(
        request,
        "devotional/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )


def current_date_devotional(request):
    current_date = timezone.now().date()
    post = Post.objects.filter(active_date=current_date, status=1).first()
    return render(request, 'devotional/index.html', 
                            {
                                'post': post,
                                #'comments': comments,
                                #'liked': likes,
                                'comment_form': CommentForm()
                            },
        )
