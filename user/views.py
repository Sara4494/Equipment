from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status  
from rest_framework.permissions import IsAuthenticated
from user.models import WORKER_SPECIALIZATIONS, CustomUser
from .serializers import CustomRegisterSerializer ,CustomTokenObtainPairSerializer, CustomUserSerializer
from rest_framework.authtoken.models import Token

class RegisterView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = CustomRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

        
            token, created = Token.objects.get_or_create(user=user)

            response_data = {
                'email': user.email,
                'user_type': user.user_type,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'profile_image': user.profile_image.url if user.profile_image else None,
                'token': token.key,  
                'message': 'User created successfully 🎉'
            }

            if user.user_type == 'worker':
                response_data['worker_specialization'] = user.worker_specialization

            return Response(response_data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class CustomLoginView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = CustomTokenObtainPairSerializer(data=request.data)

        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

 

class ProfileImageView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        if user.profile_image:
            return Response({"profile_image": user.profile_image.url})
        return Response({"error": "No profile image found"}, status=404)
    
from django.templatetags.static import static

class SpecializationsView(APIView):
    def get(self, request):
        # Creating a dictionary of specializations with icons
        specialization_icons = {
            'plumbing': static('icons/icon-2.svg'),
            'carpentry': static('icons/icon-1.svg'),
            'blacksmith': static('icons/icon-3.svg'),
            'electrician': static('icons/icon-5.svg'),
            'plaster': static('icons/icon-4.svg'),
            'painter': static('icons/icon-7.svg'),
            'general': static('icons/icon-6.svg'),
            'winch': static('icons/icon-8.svg'),
            'Ceramic': static('icons/icon-9.svg'),
        }

        # Preparing the data by adding icons
        data = [
            {
                'key': key,
                'name': name,
                'icon': specialization_icons.get(key, static('icons/default-icon.svg'))  # Provide default icon if not found
            }
            for key, name in WORKER_SPECIALIZATIONS
        ]
        
        return Response(data)
class WorkerListView(APIView):
    def get(self, request):
        specialization = request.query_params.get('specialization')  # مثلاً 'plumbing'
        workers = CustomUser.objects.filter(user_type='worker')

        if specialization:
            workers = workers.filter(worker_specialization=specialization)
        
        serializer = CustomUserSerializer(workers, many=True)
        return Response(serializer.data)





 