from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        # We need to include 'email' as a required field for registration
        fields = ('id', 'username', 'email', 'bio', 'profile_picture', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            bio=validated_data.get('bio', ''),
            profile_picture=validated_data.get('profile_picture'),
        )
        return user
    
    #["from rest_framework.authtoken.models import Token", "serializers.CharField()", "Token.objects.create", "get_user_model().objects.create_user"]