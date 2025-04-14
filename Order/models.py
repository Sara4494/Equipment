from django.db import models

from user.models import CustomUser


class Order(models.Model):
    ITEM_TYPES = [
        ('worker', 'عامل'),
        ('equipment', 'معدات'),
        ('construction', 'مواد بناء'),
    ]

    buyer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='purchases')
    seller = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='incoming_orders')
    item_type = models.CharField(max_length=20, choices=ITEM_TYPES)
    item_id = models.PositiveIntegerField()
    category = models.CharField(max_length=100)
    image = models.ImageField(upload_to='orders/', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.buyer.email} طلب من {self.seller.email} - {self.item_type}'

