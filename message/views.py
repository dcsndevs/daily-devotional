import requests
from django.shortcuts import render, get_object_or_404, reverse
from django.utils import timezone
from django.views import generic, View
from django.http import HttpResponseRedirect, HttpRequest
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Tweet, Message, TweetComment
from .forms import TweetForm, TweetCommentForm, MessageForm


class TweetList(generic.ListView):
    queryset = Tweet.objects.filter(author_id=User.id)
    template_name = "message/my-tweets.html"

class Tweets(generic.ListView):
    current_date = timezone.now().date()
    queryset = Tweet.objects.all()
    template_name = "message/index.html"

def tweet_detail(request, author):
    post = get_object_or_404(Tweet, author=author)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()
    
    if request.method == "POST":
        comment_form = TweetCommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
            request, messages.SUCCESS,
            'Comment submitted successfully!'
        )
    
    comment_form = TweetCommentForm()

    return render(
        request,
        "message/tweet_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )


def tweet_like(request, author):
    post = get_object_or_404(Tweet, author=author)
    
    if request.user in post.likes.all():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def like_comment(request, comment_id):
    comment = get_object_or_404(TweetComment, pk=comment_id)
    
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


def comment_edit(request, author, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":
        queryset = Tweet.objects.filter(status=1)
        post = get_object_or_404(queryset, author=author)
        comment = get_object_or_404(TweetComment, pk=comment_id)
        comment_form = TweetCommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Update is successful!')
        else:
            messages.add_message(request, messages.ERROR, 'Error: Could not update comment!')

    return HttpResponseRedirect(reverse('tweet_detail', args=[author]))


def comment_delete(request, author, comment_id):
    """
    view to delete comment
    """
    queryset = Tweet.objects.filter(status=1)
    post = get_object_or_404(queryset, author=author)
    comment = get_object_or_404(TweetComment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('tweet_detail', args=[author]))

class MessageList(generic.ListView):
    queryset = Message.objects.filter(author_id=User.id)
    template_name = "message/index.html"


def SendMessage(request):

    if request.method == "POST":
        message_form = MessageForm(data=request.POST)
        if message_form.is_valid():
            message_form.save()
            messages.add_message(request, messages.SUCCESS, "Message Sent")

    messages = Message.objects.filter(sender=request.user_id)
    message_form = MessageForm()

    return render(
        request,
        "about/about.html",
        {
            "messages": messages,
            "message_form": message_form
        },
    )
    