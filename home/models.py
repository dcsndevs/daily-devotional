from django.db import models


class HomeContact(models.Model):
    """
    Stores a single contact form entry.
    """

    name = models.CharField(max_length=50)
    subject = models.CharField(max_length=100)
    email = models.EmailField(max_length=60)
    message = models.CharField(max_length=500)

    def __str__(self):
        return f"Contact from {self.name}"
