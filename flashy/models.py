from django.db import models
import datetime as dt

# cloudinary
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


# Create your models here.


# subject model
class Subject(models.Model):
    name = models.CharField(max_length=100)
    image = CloudinaryField('image')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# Description model
class Notes(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
   

    # get description by user

    @classmethod
    def get_description_by_user(cls, user):
        notes = cls.objects.filter(user=user)
        return notes

    def __str__(self):
        return self.title



# profile model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    profile_pic = CloudinaryField('image')
    description = models.ManyToManyField(Notes, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.user.username