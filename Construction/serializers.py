from rest_framework import serializers
from .models import Construction, CategoryConstruction

class CategoryConstructionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryConstruction
        fields = ['id', 'name', 'image']

class ConstructionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Construction
        fields = ['id',  'price', 'description', 'image', 'category']