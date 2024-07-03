from rest_framework import generics
from rest_framework.exceptions import status
from rest_framework_simplejwt.views import TokenObtainPairView

from user.serializer import CustomTokenObtainPairSerializer, UserSerializer
from user.service import UserService
from utils import CustomResponse
# Create your views here.


class CreateUserView(generics.GenericAPIView):

    serializer_class = UserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = UserService.create_user(**serializer.validated_data)
        user = self.serializer_class(user).data
        return CustomResponse(data=user, status=status.HTTP_201_CREATED)


class CustomTokenObtainView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

        
    
