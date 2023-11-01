from django.contrib.auth import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from users.models.managers import CustomUserManager


class User(AbstractUser):
    # username = models.CharField('Никнейм', max_length=255, null=True, blank=True)
    phone_number = PhoneNumberField('Телефон', unique=True, null=True,)

    USERNAME_FIELD = 'phone_number'
    # REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
