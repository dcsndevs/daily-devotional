from django.contrib import admin
from django.contrib.auth.models import User
from .models import Membership


# Register your models here.
class MembershipAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'location', 'joined_date')
    search_fields = ('full_name', 'email', 'location')
    list_filter = ('location', 'joined_date')

admin.site.register(Membership, MembershipAdmin)