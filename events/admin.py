from django.contrib import admin
from .models import Programmes, Attendee
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Programmes)
class PostAdmin(SummernoteModelAdmin):
    """
    Lists fields for display in admin, fileds for search,
    field filters, fields to prepopulate and rich-text editor.
    """
    list_display = ('title', 'slot', 'date_of_event')
    search_fields = ('title', 'slot', 'date_of_event')
    list_filter = ('title', 'date_of_event')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('description',)


@admin.register(Attendee)
class Ateendee(admin.ModelAdmin):
    list_display = ('event', 'last_name', 'email')
    search_fields = ('last_name', 'email')
    list_filter = ('last_name', 'email')
