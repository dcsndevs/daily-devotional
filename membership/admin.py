from django.contrib import admin
from .models import Membership, Comment


# Register your models here.
admin.site.register(Membership)
admin.site.register(Comment)