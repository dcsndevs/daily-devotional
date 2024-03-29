from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from cloudinary import CloudinaryImage

from django.core.validators import RegexValidator

STATUS = ((0, "inactive"), (1, "active"))
RELATIONSHIP = ((0, "Choose not to say"), (1, "Yes"), (2, "No"), (3, "Not sure"), (4, "Married"))

class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name="owner")
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=False)
    picture = CloudinaryField('image', default='placeholder')
    bio = models.TextField(max_length=1000, null=True, blank=True)
    location = models.CharField(max_length=50, null=True, blank=True)
    where_from = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(
        max_length=20, blank=True,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',  # Example regular expression for phone number validation
                message='Phone number must be entered in the format: "+999999999". Up to 15 digits allowed.'
            ),
        ]
    )
    relationship_status = models.IntegerField(choices=RELATIONSHIP, default=0)
    favourite_scripture = models.CharField(max_length=500, null=True, blank=True)
    favourite_bible_character = models.CharField(max_length=50, null=True, blank=True)
    education = models.CharField(max_length=100, null=True, blank=True)
    handle = models.CharField(max_length=50, null=True, blank=True)
    joined_date = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=1)
    
    
    class Meta:
        ordering = ['-joined_date']
        
    def __str__(self):
        return f"{self.owner} | {self.first_name} Joined {self.joined_date}"
    
    def get_cloudinary_image(self):
        """
        Method to retrieve the CloudinaryImage representation of the picture.
        """
        if self.picture:
            return CloudinaryImage(self.picture).image()
        else:
            return None