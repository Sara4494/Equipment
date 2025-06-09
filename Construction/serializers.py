from rest_framework import serializers
from .models import Construction, CategoryConstruction

class CategoryConstructionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryConstruction
        fields = ['id', 'name', 'image']

class ConstructionSerializer(serializers.ModelSerializer):
    phone = serializers.SerializerMethodField()  

    class Meta:
        model = Construction
        fields = ['id', 'price', 'description', 'image', 'category', 'rating', 'phone']   

    def get_phone(self, obj):  # لازم يكون اسمه get_phone عشان يماتش الـ field
        return obj.owner.phone