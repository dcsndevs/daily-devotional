import requests
from django.shortcuts import render, get_object_or_404, reverse
from django.utils import timezone
from django.views import generic, View
from django.http import HttpResponseRedirect, HttpRequest
from django.utils import timezone
from django.contrib import messages
from .models import Post, Comment
from .forms import CommentForm


class PostList(generic.ListView):
    current_date = timezone.now().date()
    queryset = Post.objects.filter(active_date__lte=current_date, status=1)
    template_name = "devotional/archive.html"
    paginate_by = 12  


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
    if post:
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
        
        return render(request, 'devotional/index.html', 
                                {
                                    'post': post,
                                    "comments": comments,
                                    "comment_count": comment_count,
                                    'comment_form': CommentForm()
                                },
            )
    else:
        return HttpResponseRedirect('archive', messages.add_message(
                request, messages.SUCCESS,
                'No Post for today yet.'
            ))


def post_like(request, slug):
    post = get_object_or_404(Post, slug=slug)
    
    if request.user in post.likes.all():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def like_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    
    # Check if the user has already liked the comment
    if request.user in comment.likes2.all():
        # User has already liked the comment, so unlike it
        comment.likes2.remove(request.user)
        liked = False
    else:
        # User hasn't liked the comment yet, so like it
        comment.likes2.add(request.user)
        liked = True
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updat is successful!')
        else:
            messages.add_message(request, messages.ERROR, 'Error: Could not update comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))

def view_verse(request, scripture):
    # Make request to Bible API with KJV translation and verse numbers
    api_url = f'https://bible-api.com/{scripture}?translation=kjv&verse_numbers=true'
    response = requests.get(api_url)
    if response.status_code == 200:
        verse_data = response.json()
        book_name = verse_data['verses'][0]['book_name']
        chapter = verse_data['verses'][0]['chapter']
        verses = verse_data['verses']
        verse_text = "\n".join([f"{verse['verse']}. {verse['text']}" for verse in verses])
        return render(request, 'devotional/view_verse.html', {'book_name': book_name, 'chapter': chapter, 'verse_text': verse_text})
    else:
        return render(request, 'devotional/view_verse.html', {'error': 'Verse not found'})
