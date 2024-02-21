from django.contrib import admin
from .models import Programmes, Guest, MemberGuest
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Programmes)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slot', 'date_of_event')
    search_fields = ('title', 'slot', 'date_of_event')
    list_filter = ('title', 'date_of_event')

@admin.register(Guest, MemberGuest)
class Ateendee(admin.ModelAdmin):
    list_display = ('event', 'last_name', 'email')
    search_fields = ('last_name', 'email')
    list_filter = ('last_name', 'email')