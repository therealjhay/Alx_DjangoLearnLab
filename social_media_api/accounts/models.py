from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True)
    followers = models.ManyToManyField(
        'self', 
        symmetrical=False, 
        related_name='followers_list', 
        blank=True
    )
    
    following = models.ManyToManyField(
        'self', 
        symmetrical=False, 
        related_name='following_list', 
        blank=True
    )
    # Add related_name to resolve clashes
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )
    
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username