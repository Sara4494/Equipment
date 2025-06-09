from rest_framework import serializers
from .models import Equipment, CategoryEquipment

class CategoryEquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryEquipment
        fields = ['id', 'name', 'image']

class EquipmentSerializer(serializers.ModelSerializer):
    phone = serializers.SerializerMethodField()  

    class Meta:
        model = Equipment
        fields = ['id', 'price', 'description', 'image', 'category', 'rating', 'phone']   

    def get_phone(self, obj): 
        return obj.owner.phone

