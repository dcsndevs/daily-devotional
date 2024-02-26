from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Tweet, TweetComment, Message
    
# Register your models here.
@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    
    list_display = ('author', 'created_on')
    search_fields = ('author', 'message')
    
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    
    list_display = ('author', 'created_on')
    search_fields = ('author', 'message')

@admin.register(TweetComment)
class CommentAdmin(admin.ModelAdmin):
    
    list_display = ('post', 'author', 'created_on')
    search_fields = ('post', 'author', 'body')

