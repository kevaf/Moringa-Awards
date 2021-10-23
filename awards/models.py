from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    profpic = models.ImageField(upload_to = 'images/')
    bio = models.TextField(max_length=1000)
    about = models.TextField(max_length=5000)


    def __str__(self):
        return self.username

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

class Projects(models.Model):
    title = models.CharField(max_length=500)
    description=models.TextField(max_length=2000)
    link=models.URLField()
    image=models.ImageField(upload_to='images/')
    user = models.ForeignKey(User,on_delete = models.CASCADE)

