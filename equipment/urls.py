from django.urls import path
from .views import CategoryListAPIView, EquipmentByCategoryAPIView, EquipmentCreateAPIView

urlpatterns = [
    path('categories/', CategoryListAPIView.as_view(), name='category-list'),
    path('categories/<int:category_id>/equipments/', EquipmentByCategoryAPIView.as_view(), name='equipment-by-category'),
    path('equipments/create/', EquipmentCreateAPIView.as_view(), name='equipment-create'),
]
