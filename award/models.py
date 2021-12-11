from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import cloudinary
from cloudinary.models import CloudinaryField
import datetime as dt

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(blank=True, max_length=120)
    profile_picture = CloudinaryField('image')
    bio = models.TextField(max_length=500, default="My Bio", blank=True)
    location = models.CharField(max_length=60, blank=True)
    contact = models.EmailField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    # def save_profile(self):
    #     self.user

    # def delete_profile(self):
    #     self.delete()

    # @classmethod
    # def search_profile(cls, name):
    #     return cls.objects.filter(user__username__icontains=name).all()