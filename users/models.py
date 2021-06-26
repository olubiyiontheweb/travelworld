from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserAccount(AbstractUser):
    id = models.BigAutoField(primary_key=True)
    email = models.EmailField(unique=True)
    term_of_service = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['term_of_service']
