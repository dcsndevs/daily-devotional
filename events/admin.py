from django.contrib import admin
from .models import Event, Ateendee, MemberAteendee


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'slot', 'date_of_event')
    search_fields = ('title', 'slot', 'date_of_event')
    list_filter = ('title', 'date_of_event')

@admin.register(Ateendee, MemberAteendee)
class Ateendee(admin.ModelAdmin):
    list_display = ('event', 'last_name', 'email')
    search_fields = ('last_name', 'email')
    list_filter = ('last_name', 'email')