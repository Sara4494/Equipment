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
    ('material_supplier', 'مورد مواد بناء'),
]

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    governorate = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    user_type = models.CharField(max_length=20, choices=USER_TYPES)
    profile_image = models.ImageField(upload_to='profiles/', blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    objects = CustomUserManager()
    USERNAME_FIELD = 'email'  # التأكيد أن 'email' هو الحقل المستخدم كاسم المستخدم
    REQUIRED_FIELDS = []  # لا يتم تضمين 'username'

    def __str__(self):
        return self.email


    

class Equipment(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'user_type': 'equipment_owner'})
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='equipment/')

 