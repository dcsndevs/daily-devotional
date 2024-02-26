from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Tweet, Message
    
# Register your models here.
@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    
    list_display = ('author', 'created_on', 'message')
    search_fields = ('author', 'message')
    
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    
    list_display = ('author', 'created_on', 'message')
    search_fields = ('author', 'message')
