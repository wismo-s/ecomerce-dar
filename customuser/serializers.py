from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import get_user_model, authenticate
from django.core.exceptions import ValidationError

USER_MODEL = get_user_model()

class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = USER_MODEL
        fields = ('username', 'email', 'first_name', 'last_name',)
        
        
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('distric', 'department', 'reference', 'direction', 'phone', 'postal_code',)
        
class CustomUserCreateSerializer(serializers.Serializer):
    class Meta:
        pass
    
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField(max_length=150)
    first_name = serializers.CharField(max_length=150)
    last_name = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=150)
    distric = serializers.CharField(max_length=125, allow_null=True, allow_blank=True, default='')
    department = serializers.CharField(max_length=80, allow_null=True, allow_blank=True, default='')
    reference = serializers.CharField(max_length=150, allow_null=True, allow_blank=True, default='')
    direction = serializers.CharField(max_length=300, allow_null=True, allow_blank=True, default='')
    phone = serializers.CharField(max_length=20)
    postal_code = serializers.CharField(max_length=10, allow_null=True, allow_blank=True, default='')
    
    def create(self, validated_data):
        user_intance = USER_MODEL.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user_intance.set_password(validated_data['password'])
        user_intance.save()
        customUser = CustomUser.objects.create(
            user=user_intance, 
            distric=validated_data['distric'], 
            department=validated_data['department'], 
            reference=validated_data['reference'], 
            direction=validated_data['direction'], 
            phone=validated_data['phone'], 
            postal_code=validated_data['postal_code']
            )
        return customUser
    
class LoginSerializer(serializers.Serializer):
    class Meta:
        model = USER_MODEL
        fields = ['username', 'password']
        
    def auth(self, data):
        username = data.get('username')
        password = data.get('password')
        user = authenticate(username=username, password=password)
        if not user:
            raise serializers.ValidationError('usuario no encontrado')
        return user
    