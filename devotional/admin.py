from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


class CustomUserAdmin(BaseUserAdmin):
    list_filter = ('is_active', 'is_superuser', 'date_joined')
    list_display = ('username', 'is_active', 'first_name', 'last_name', 'email')


# Register your models here.
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Lists fields for display in admin, fileds for search,
    field filters, fields to prepopulate and rich-text editor.
    """

    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug', 'status', 'active_date')
    search_fields = ['title', 'content']
    list_filter = ('status', 'active_date',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content', 'memory_verse')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Lists fields for display in admin, fileds for comment search,
    field filters, fields to prepopulate and rich-text editor.
    """

    list_display = ('author', 'body', 'post', 'created_on')
    list_filter = ('approved', 'created_on')
    search_fields = ('author', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=False)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
