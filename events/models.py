from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

APPROVED = ((1, "True"), (0, "False"))
STATUS = ((1, "True"), (0, "False"))

class Event(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="event_posts")
    slug = models.SlugField(max_length=250, unique=True)
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField(max_length=1000, null=True, blank=True)
    slot = models.PositiveIntegerField(null=True, blank=True)
    date_of_event = models.DateField()
    created_on = models.DateTimeField()
    registration_expires = models.DateTimeField(null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    banner = CloudinaryField('image', default='placeholder3')
    status = models.IntegerField(choices=STATUS, default=1)
    

class Ateendee(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="anonymous_attendees")
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    newsletter = models.IntegerField(choices=APPROVED, default=1)


class MemberAteendee(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="profiled_member_attendees")
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(unique=True)
    newsletter = models.IntegerField(choices=APPROVED, default=1)
