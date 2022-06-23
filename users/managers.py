from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, username, country, gender,account_type, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email), username=username, gender=gender, country=country , account_type = account_type
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, country, gender,account_type, password):
        """Create and save a new superuser with given details"""

        user = self.create_user(email, username, country, gender,account_type, password)

        user.admin = True
        user.staff = True

        user.save(using=self._db)
        return user
