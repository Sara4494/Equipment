from rest_framework import serializers
from .models import WORKER_SPECIALIZATIONS, CustomUser 
from django.contrib.auth import get_user_model  
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    profile_image = serializers.ImageField(required=True)
    worker_specialization = serializers.ChoiceField(
        choices=WORKER_SPECIALIZATIONS, required=False, allow_blank=True
    )

    class Meta:
        model = get_user_model()
        fields = [
            'first_name', 'last_name', 'email', 'phone', 'governorate', 'city',
            'user_type', 'worker_specialization', 'profile_image', 'password', 'password_confirmation'
        ]

    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirmation']:
            raise serializers.ValidationError("Passwords must match")

        if attrs['user_type'] == 'worker' and not attrs.get('worker_specialization'):
            raise serializers.ValidationError("يجب اختيار نوع العامل")

        attrs.pop('password_confirmation')
        return attrs

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = get_user_model().objects.create_user(**validated_data)
        user.set_password(password)
        user.save()
        return user


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    email = serializers.EmailField()  
    password = serializers.CharField(write_only=True)   

    def validate(self, attrs):
        User = get_user_model()

        try:
        
            user = User.objects.get(email=attrs['email'])
        except User.DoesNotExist:
            raise serializers.ValidationError("البريد الإلكتروني غير مسجل")

        if not user.check_password(attrs['password']):
            raise serializers.ValidationError("كلمة السر غير صحيحة")

        attrs['user'] = user
        attrs['user_type'] = user.user_type  
        
        return attrs  

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['user_type'] = user.user_type
        token['email'] = user.email
        return token


from rest_framework import serializers
from .models import CustomUser
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser 
        fields = ('first_name', 'last_name',   'governorate', 'city',  'worker_specialization', 'profile_image')