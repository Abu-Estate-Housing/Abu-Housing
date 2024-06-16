from django.contrib.auth.models import BaseUserManager
from django.db.models.manager import BaseManager
from django.utils.text import gettext_lazy

class CustomAccountManager(BaseUserManager):
    def create_user(
            self, email, username, first_name, password, **kwargs
    ):
        if not email:
            raise ValueError(gettext_lazy("You must provide an email address"))
        email = self.normalize_email(email)
        print("Creating user")
        print(f"Email {email} Password {password}")
        user = self.model(email=email, username=username, first_name=first_name, **kwargs)
        print("Created user", user)
        user.set_password(password)
        user.save()
        print("User Saved")
        return user

    def create_superuser(
            self, email, username, first_name, password, **kwargs
    ):
        if not email:
            raise ValueError(gettext_lazy("You must provide an email address"))
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_active", True)
        kwargs.setdefault("is_superuser", True)
        return self.create_user(email, username, first_name, password, **kwargs)
