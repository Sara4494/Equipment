from django.urls import path
from .views import RegisterView, CustomLoginView , ProfileImageView , WorkerListView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),              # تسجيل حساب جديد
    path('login/', CustomLoginView.as_view(), name='custom_login'),
     path('profile-image/', ProfileImageView.as_view(), name='profile-image'),    
     path('workers/', WorkerListView.as_view(), name='worker-list'),
              
  
  
]
