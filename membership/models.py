from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "inactive"), (1, "active"))

class Membership(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name="owner")
    full_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    picture = CloudinaryField('image', default='placeholder')
    bio = models.TextField()
    location = models.CharField(max_length=50)
    phone = models.IntegerField()
    joined_date = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=1)
    
    
    class Meta:
        ordering = ['-joined_date']
        
    def __str__(self):
        return f"{self.owner} | {self.full_name} Joined {self.joined_date}"