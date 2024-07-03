"""User service module."""
from user.models import User


class UserService:
    """User application services."""

    @staticmethod
    def create_user(**data):
        """Create a new user."""
        user = User.objects.create_user(**data)
        return user
