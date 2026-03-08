from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, username, phone, password=None, **extra_fields):
        if not username:
            raise ValueError("Никнейм обязателен")
        if not phone:
            raise ValueError("Телефон обязателен")
        user = self.model(username=username, phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, phone, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, unique=True)
    phone = models.CharField(max_length=20, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['phone']

    def __str__(self):
        return self.username
