from django.db import models
from user.models import CustomUser


class CategoryConstruction(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='icon/')

    def __str__(self):
        return self.name
    
class Construction(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'user_type': 'construction_owner'})
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='construction_imeges/')
    category = models.ForeignKey(CategoryConstruction, on_delete=models.CASCADE)



