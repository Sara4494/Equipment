from django.db import models


class CategoryConstruction(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='icon/')

    def __str__(self):
        return self.name
    


class Construction(models.Model):
    
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='construction/')
    category = models.ForeignKey(CategoryConstruction, on_delete=models.CASCADE)



