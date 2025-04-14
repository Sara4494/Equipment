from rest_framework import serializers
from .models import Order
class OrderSerializer(serializers.ModelSerializer):
    buyer_name = serializers.SerializerMethodField()
    class Meta:
        model = Order
        fields = ['id', 'item_type', 'item_id', 'category', 'image', 'price', 'created_at', 'buyer_name']

    def get_buyer_name(self, obj):
        return f"{obj.buyer.first_name} {obj.buyer.last_name}"
