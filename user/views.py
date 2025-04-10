from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status  
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from user.models import CustomUser
from .serializers import CustomRegisterSerializer ,CustomTokenObtainPairSerializer, CustomUserSerializer
class RegisterView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = CustomRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            response_data = {
                'email': user.email,
                'user_type': user.user_type,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'profile_image': user.profile_image.url if user.profile_image else None,
                'message': 'User created successfully'
            }

            if user.user_type == 'worker':
                response_data['worker_specialization'] = user.worker_specialization

            return Response(response_data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
class CustomLoginView(APIView):
    def post(self, request, *args, **kwargs):
 
        serializer = CustomTokenObtainPairSerializer(data=request.data)

        if serializer.is_valid():
       
            return Response({
                'token': serializer.validated_data['token'],   
                'user_type': serializer.validated_data['user_type'],   
            }, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


 

class ProfileImageView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        if user.profile_image:
            return Response({"profile_image": user.profile_image.url})
        return Response({"error": "No profile image found"}, status=404)
    

class WorkerListView(APIView):
    def get(self, request):
        workers = CustomUser.objects.filter(user_type='worker')

        # للتأكد من البيانات المسترجعة
        if workers.exists():
            print("Workers Found:", workers)
        else:
            print("No workers found.")

        # استخدام serializer لتحويل البيانات إلى JSON
        serializer = CustomUserSerializer(workers, many=True)
        return Response(serializer.data)
