from django.urls import path
from .views import RegisterView, CustomLoginView , ProfileImageView, SpecializationsView , WorkerListView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),             
    path('login/', CustomLoginView.as_view(), name='custom_login'),
     path('profile-image/', ProfileImageView.as_view(), name='profile-image'),   
   path('specializations/', SpecializationsView.as_view(), name='specializations'),

 
     path('workers/', WorkerListView.as_view(), name='worker-list'),
               
]
