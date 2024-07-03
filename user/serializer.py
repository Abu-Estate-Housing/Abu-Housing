from rest_framework import serializers

from user.models import User

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserSerializer(serializers.ModelSerializer):
    """Serializes the user model."""

    password = serializers.CharField(write_only=True)

    class Meta:
        """Define the meta data that is contained in api response."""

        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "username",
            "email",
            "phone",
            "password",
        ]



class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data['user'] = UserSerializer(self.user).data 
        return data
        
    
