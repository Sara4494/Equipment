from django.urls import path
from .views import (
    CreateOrderAPIView,
    MyPurchasesAPIView,
    IncomingOrdersAPIView,
)

urlpatterns = [
    path('create/', CreateOrderAPIView.as_view(), name='create-order'),
    path('my-purchases/', MyPurchasesAPIView.as_view(), name='my-purchases'),
    path('incoming/', IncomingOrdersAPIView.as_view(), name='incoming-orders'),
]
