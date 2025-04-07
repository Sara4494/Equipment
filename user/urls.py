from django.urls import path
from .views import RegisterView, CustomLoginView, EquipmentCreateView, EquipmentListView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),              # تسجيل حساب جديد
    path('login/', CustomLoginView.as_view(), name='custom_login'),          # تسجيل دخول مخصص بالإيميل
    path('equipment/create/', EquipmentCreateView.as_view(), name='equipment-create'),  # إنشاء معدة
    path('equipment/', EquipmentListView.as_view(), name='equipment-list'),  # عرض كل المعدات
]
