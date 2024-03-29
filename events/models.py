from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "draft"), (1, "published"))


class Programmes(models.Model):
    """
    Stores a single blog post entry related to :model:`auth.User`.
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="event_posts")
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

    class Meta:
        ordering = ['-registration_expires']

    def __str__(self):
        return f"{self.date_of_event} | {self.title}"


class Attendee(models.Model):
    """
    Stores a single comment entry related to :model:`auth.User`
    and :model:`Programmes.Post`.
    """
    event = models.ForeignKey(Programmes, on_delete=models.CASCADE,
                              related_name="anonymous_attendee")
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=False)
    newsletter = models.BooleanField(default=False)
