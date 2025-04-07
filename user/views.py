from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomRegisterSerializer

 
from rest_framework import generics, permissions
from .serializers import CustomRegisterSerializer, EquipmentSerializer
from .models import Equipment
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
class RegisterView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = CustomRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                'email': user.email,
                'user_type': user.user_type,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'profile_image': user.profile_image.url ,
                'message': 'User created successfully'
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EquipmentCreateView(generics.CreateAPIView):
    serializer_class = EquipmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class EquipmentListView(generics.ListAPIView):
    serializer_class = EquipmentSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return Equipment.objects.all()

 
from rest_framework.response import Response
from rest_framework import status
from .serializers import CustomTokenObtainPairSerializer

class CustomLoginView(APIView):
    def post(self, request, *args, **kwargs):
 
        serializer = CustomTokenObtainPairSerializer(data=request.data)

        if serializer.is_valid():
       
            return Response({
                'token': serializer.validated_data['token'],   
                'user_type': serializer.validated_data['user_type'],   
            }, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# {
#     "email": "sryad5514@gmail.com",
#     "password": "شيةهىج123د"
# }