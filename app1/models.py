from django.contrib.auth.models import AbstractUser
from django.db import models

class UserProfile(AbstractUser):
    email = models.EmailField(unique=True)

    # Provide unique related_name for groups and user_permissions
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='user_profiles',
        related_query_name='user_profile',
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='user_profiles',
        related_query_name='user_profile',
        blank=True,
    )

    def __str__(self):
        return self.username
