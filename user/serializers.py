from rest_framework import serializers
from .models import WORKER_SPECIALIZATIONS, CustomUser 
from django.contrib.auth import get_user_model  
from rest_framework.authtoken.models import Token

class CustomRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    profile_image = serializers.ImageField(required=True)
    worker_specialization = serializers.ChoiceField(
        choices=WORKER_SPECIALIZATIONS, required=False, allow_blank=True
    )
    price = serializers.DecimalField(max_digits=10, decimal_places=2, required=False, allow_null=True)  # السعر هنا

    class Meta:
        model = get_user_model()
        fields = [
            'first_name', 'last_name', 'email', 'phone', 'governorate', 'city',
            'user_type', 'worker_specialization', 'profile_image', 'password', 'password_confirmation', 'price'
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

User = get_user_model()

class CustomTokenObtainPairSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid email or password")

        if not user.check_password(password):
            raise serializers.ValidationError("Invalid email or password")

        token, _ = Token.objects.get_or_create(user=user)

        return {
            'token': token.key,
            'user_type': user.user_type,
            'email': user.email,

           
        }

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['user_type'] = user.user_type
        token['email'] = user.email
        return token

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser 
        fields = ('first_name', 'last_name', 'price',  'governorate', 'city',  'worker_specialization', 'profile_image')