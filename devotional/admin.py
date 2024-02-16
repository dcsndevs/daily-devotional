from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

    
# Register your models here.
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug', 'status', 'active_date')
    search_fields = ['title', 'content']
    list_filter = ('status', 'active_date',)
    summernote_fields = ('content', 'memory_verse')
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    
    list_display = ('author', 'body', 'post', 'created_on')
    list_filter = ('approved', 'created_on')
    search_fields = ('author', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=False)

