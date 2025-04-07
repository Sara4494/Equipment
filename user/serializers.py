from rest_framework import serializers
from .models import CustomUser, Equipment
from django.contrib.auth import get_user_model  
 
class CustomRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    profile_image = serializers.ImageField(required=True)

    class Meta:
        model = get_user_model()
        fields = [ 'first_name', 'last_name','email',  'phone','governorate','city','user_type',  'profile_image','password', 'password_confirmation' ]
    
    def validate(self, attrs):
        # تحقق من تطابق كلمة المرور
        if attrs['password'] != attrs['password_confirmation']:
            raise serializers.ValidationError("Passwords must match")
        
        # حذف password_confirmation لأنها ليست جزءًا من الموديل
        attrs.pop('password_confirmation')
        return attrs

    def create(self, validated_data):
        # استخراج كلمة المرور
        password = validated_data.pop('password')
        # إنشاء المستخدم
        user = get_user_model().objects.create_user(**validated_data)
        # تعيين كلمة السر بشكل آمن
        user.set_password(password)
        user.save()
        return user




class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = '__all__'

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
  

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    email = serializers.EmailField()  # إضافة حقل الإيميل
    password = serializers.CharField(write_only=True)  # حقل الباسورد

    def validate(self, attrs):
        User = get_user_model()

        try:
            # البحث عن المستخدم باستخدام الإيميل
            user = User.objects.get(email=attrs['email'])
        except User.DoesNotExist:
            raise serializers.ValidationError("البريد الإلكتروني غير مسجل")

        # التحقق من كلمة السر
        if not user.check_password(attrs['password']):
            raise serializers.ValidationError("كلمة السر غير صحيحة")
        
        # إضافة user_type في attrs ليكون متاحًا في validated_data
        attrs['user'] = user
        attrs['user_type'] = user.user_type  # إضافة user_type في attrs
        
        return attrs  # لازم نرجع attrs بعد التحقق

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['user_type'] = user.user_type
        token['email'] = user.email
        return token
