from django.contrib.auth.models import BaseUserManager
from django.utils.text import gettext_lazy

class CustomAccountManager(BaseUserManager):
    def create_user(
            self, email, **kwargs
    ):
        if not email:
            raise ValueError(gettext_lazy("You must provide an email address"))
        email = self.normalize_email(email)
        print("Creating user")
        print(f"Kwargs {kwargs}")
        password = kwargs.get('password')
        print(f"Email {email} Password {password}")
        user = self.model(email=email, **kwargs)
        print("Created user", user)
        user.set_password(password)
        user.save(using=self._db)
        print("User Saved")
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
