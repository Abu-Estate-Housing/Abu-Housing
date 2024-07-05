from django.contrib.auth.models import BaseUserManager
from django.utils.text import gettext_lazy

class CustomAccountManager(BaseUserManager):
    def create_user(
            self, email, **kwargs
    ):
        if not email:
            raise ValueError(gettext_lazy("You must provide an email address"))
        email = self.normalize_email(email)
        password = kwargs.get('password')
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
            self, email, **kwargs
    ):
        if not email:
            raise ValueError(gettext_lazy("You must provide an email address"))
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_active", True)
        kwargs.setdefault("is_superuser", True)
        return self.create_user(email, **kwargs)
