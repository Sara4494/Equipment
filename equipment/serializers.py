from rest_framework import serializers
from .models import Equipment, CategoryEquipment

class CategoryEquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryEquipment
        fields = ['id', 'name', 'image']

class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = ['id', 'name', 'price', 'description', 'image', 'category']