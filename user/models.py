from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

USER_TYPES = [
    ('worker', 'عامل'),
    ('contractor', 'مقاول'),
    ('equipment_owner', 'صاحب معدات'),
 
]

WORKER_SPECIALIZATIONS = [
    ('plumbing', 'عامل سباكة'),
    ('carpentry', 'عامل نجارة'),
    ('blacksmith', 'عامل حدادة'),
    ('electrician', 'عامل كهرباء'),
    ('plaster', 'عامل محارة'),
    ('painter', 'عامل نقاشة'),
    ('general', 'عامل عام'),
    ('winch', 'عامل ونش'),
    ('Ceramic', 'عامل سرميك'),
]


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    governorate = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    user_type = models.CharField(max_length=20, choices=USER_TYPES)
    worker_specialization = models.CharField(
        max_length=20, choices=WORKER_SPECIALIZATIONS, blank=True, null=True
    )
    profile_image = models.ImageField(upload_to='profiles/', blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


    
 
 