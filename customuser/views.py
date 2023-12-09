from rest_framework import views
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import login, logout
from rest_framework.authtoken.models import Token
from .models import CustomUser
from .serializers import CustomUserCreateSerializer, LoginSerializer, UserModelSerializer, CustomUserSerializer

# Create your views here.
class CustomUserCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = CustomUserCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Usuario creado correctamente'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class CustomUserView(views.APIView):
    
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            user = request.user
            serializer = UserModelSerializer(user)
            extra_data = CustomUser.objects.get(user=user)
            serializer_extradata = CustomUserSerializer(extra_data)
            response = {**serializer.data, **serializer_extradata.data}
            return Response(response, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'User is not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)
        
    def put(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            user = request.user
            serializer = CustomUserCreateSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Usuario actualizado correctamente'}, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': 'User is not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)
        
    def delete(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            user = request.user
            user.delete()
            return Response({'message': 'Usuario eliminado correctamente'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'User is not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)     

class CustomUserLoginView(views.APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        serilizer = LoginSerializer(data=data)
        if serilizer.is_valid(raise_exception=True):
            user = serilizer.auth(data=data)
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({'message': 'ingreso correctamente', 'user': serilizer.data, 'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'el usuario o contrasena no es corretco'}, status=status.HTTP_404_NOT_FOUND)

class CustomUserLogoutView(views.APIView):
    def post(self, request, *args, **kwargs):
        logout(request)
        return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)