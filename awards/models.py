from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    dpic = models.ImageField(upload_to = 'images/')
    bio = models.TextField(max_length=1000)
    info = models.TextField(max_length=5000)