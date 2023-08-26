from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


# Create your models here.
class User(AbstractUser):
    """
    Model for representing a user in the system.

    Fields:
    - email (EmailField): Email address of the user. Used for authentication.
    - phone (PositiveIntegerField): Phone number of the user.
    - city (CharField): City where the user is located.
    - avatar (ImageField): Avatar image of the user.
    """
    username = None
    email = models.EmailField(max_length=50, verbose_name='почта', unique=True)
    phone = models.PositiveIntegerField(verbose_name='телефон', unique=True, **NULLABLE)
    city = models.CharField(max_length=50, verbose_name='город', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []