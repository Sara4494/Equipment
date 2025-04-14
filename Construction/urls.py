from django.urls import path
from .views import CategoryListAPIView, ConstructionListAPIView , ConstructionCreateAPIView

urlpatterns = [
    path('categories_construction/', CategoryListAPIView.as_view(), name='category-list'),
    path('construction_list/', ConstructionListAPIView.as_view(), name='equipment-by-category'),
    path('create/', ConstructionCreateAPIView.as_view(), name='equipment-create'),
  
]
