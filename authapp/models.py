from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    email = models.EmailField(verbose_name='email', max_length=255, unique=True)
    phone = models.CharField(null=True, max_length=255)
    username = models.TextField(verbose_name='username', max_length=255, unique=True)
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'phone']
    USERNAME_FIELD = 'email'

    def get_username(self):
        return self.email
