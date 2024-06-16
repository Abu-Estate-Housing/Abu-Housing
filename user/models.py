from django.contrib.auth.models import AbstractUser, PermissionsMixin

from django.db import models
from django.utils.text import gettext_lazy

from user.custom_user_manager import CustomAccountManager

class User(AbstractUser, PermissionsMixin):
    Roles: tuple = ((1, "Admin"), (2, "Tenant"), (3, "Landlord"))
    first_name = models.CharField(max_length=20, null=False)
    last_name = models.CharField(max_length=20, null=False)
    username = models.CharField(max_length=20, unique=True, null=False)
    email = models.CharField(gettext_lazy("email address"), max_length=30, unique=True, null=False)
    phone = models.CharField(max_length=20, null=False)
    about = models.TextField(gettext_lazy("about"), max_length=500, blank=True)
    role = models.PositiveSmallIntegerField(choices=Roles, null=False, default=1)
    is_active = models.BooleanField(default=True)
    objects = CustomAccountManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        'username', 'first_name'
    ]

    def __str__(self):
        return f"{self.first_name }"

class Landlord(User):
    class Meta:
        proxy = True
        verbose_name = "Landlord"
        verbose_name_plural = "Landlords"
