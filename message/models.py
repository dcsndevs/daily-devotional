from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Tweet(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="tweets", default=1, null=False)
    message = models.TextField(max_length=200, null=True, blank=True)
    image = CloudinaryField('image', default='placeholder')
    likes = models.ManyToManyField(User, related_name="tweet_likes", blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_on']
    
    def __str__(self):
        return f"{self.author} | {self.created_on}"
    
    def number_of_likes(self):
        return self.likes.count()

class TweetComment(models.Model):
    post = models.ForeignKey(Tweet, on_delete=models.CASCADE, related_name="tweet_comments", null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tweet_commenter", null=True, blank=True)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    likes2 = models.ManyToManyField(User, related_name="tweet_comment_likes", blank=True)
    
    @property
    def likes2_count(self):
        return self.likes2.count()

    class Meta:
        ordering = ['-created_on']
    
        
    def __str__(self):
        return f"Comment by {self.author}"
    
    def number_of_likes2(self):
        return self.likes2.count()
    
    
class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="messages", default=1, null=False)
    sender = models.ForeignKey(User, on_delete=models.DO_NOTHING,
                               related_name="outbox", default=1, null=False)
    message = models.TextField(max_length=200, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_on']
    
    def __str__(self):
        return f"{self.author} to {self.sender}| {self.created_on}"

class Contacts(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="contacts", null=True, blank=True)
    friend = models.ManyToManyField(User, related_name="friend", blank=True)