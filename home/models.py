from django.db import models

# Create your models here.
class HomeContact(models.Model):
    
    name = models.CharField(max_length=50)
    subject = models.CharField(max_length=100)
    email = models.EmailField(max_length=60)
    message = models.CharField(max_length=500)
    
 
    def __str__(self):
        return f"Contact from {self.name}"