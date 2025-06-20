from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser

class RoleChoices(models.TextChoices):

    ADMIN = 'Admin' , 'Admin'

    USER = 'User' , 'User'

class Profile(AbstractUser):

    role = models.CharField(max_length=10,choices=RoleChoices.choices)

    def _str_(self):

        return self.email
    
    class Meta :

        verbose_name = 'Profile'

        verbose_name_plural = 'Profile'