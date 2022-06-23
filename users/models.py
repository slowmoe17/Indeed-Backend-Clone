from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager

class User(AbstractBaseUser):
    class account(models.TextChoices):
        employee = "employee"
        employer = "employer"

    genders = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    email = models.EmailField(max_length=100, unique=True)
    account_type = models.CharField(max_length=10, choices=account.choices, default=account.employee)
    username = models.CharField(max_length=20)
    gender = models.CharField(max_length=1,choices=genders)
    country = models.CharField(max_length=20, blank=True, null=True)
    

    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "gender","account_type","country"]

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their username
        return self.username

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
    
    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

class EmployeeProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=100, blank=True, null=True)
    bio = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=100,null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/',null=True, blank=True)

    @property
    def get_job_title(self):
        return self.job_title

class EmployerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    company_description = models.TextField()
    location = models.CharField(max_length=100)
    company_logo = models.ImageField(upload_to='company_logos/', blank=True)

