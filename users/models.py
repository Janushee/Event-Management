from django.db import models
from django.contrib.auth.models import AbstractUser

ROLE_CHOICES = (
    ("admin", "admin"),
    ("user", "user")
)
# Create your models here.
class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255,unique=True)
    password = models.CharField(max_length=255)
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='user'
    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []