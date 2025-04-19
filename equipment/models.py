from django.db import models
from user.models import CustomUser
from django.core.validators import MinValueValidator, MaxValueValidator

class CategoryEquipment(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='icon/')

    def __str__(self):
        return self.name

class Equipment(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'user_type': 'equipment_owner'})

    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='equipment/')
    category = models.ForeignKey(CategoryEquipment, on_delete=models.CASCADE)
    rating = models.IntegerField(
        null=True, blank=True,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text="قيم من 1 إلى 5"
    )



