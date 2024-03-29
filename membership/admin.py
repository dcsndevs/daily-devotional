from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile


# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    """
    Lists fields for display in admin, fileds for search,
    field filters, fields to prepopulate and rich-text editor.
    """
    list_display = ('first_name', 'email', 'location', 'joined_date')
    search_fields = ('first_name', 'email', 'location')
    list_filter = ('location', 'joined_date')

admin.site.register(Profile, ProfileAdmin)