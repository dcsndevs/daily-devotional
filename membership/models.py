from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "draft"), (1, "published"))
APPROVED = ((0, "True"), (1, "False"))
