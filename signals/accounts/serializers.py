from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=100, write_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'phone']
        
    def create(self, validated_data):
        user = User.objects.create_user(
            username = validated_data['username'],
            email = validated_data['email'],
            phone = validated_data['phone']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.phone = validated_data.get('phone', instance.phone)
        
        password = validated_data.get('password')
        if password:
            instance.set_password(password)
            
        instance.save()
        return instance
    
    def delete(self, instance):
        instance.delete()
        return instance
        

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'user', 'bio']