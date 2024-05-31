from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class Profile(models.Model):
    """
        Profile Model for users
    """
    user = models.ForeignKey(User, related_name='profile', on_delete=models.CASCADE)
    image = ResizedImageField(
        upload_to='profileImages/',
        default='defaultProfile.png',
        force_format='webp',
        null=True,
        quality=75,
        size=[300, 300],
        blank=True)
    bio = models.TextField(max_length=2500, blank=True)
    name = models.CharField(max_length=100, blank=True)
    lastname = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=100, blank=True)
    joined_on = models.DateTimeField(auto_now_add=True)
    hobbys = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
