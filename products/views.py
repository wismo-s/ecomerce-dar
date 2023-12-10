from django.shortcuts import render
from rest_framework import views
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAdminUser, AllowAny
from .models import Products, Category, Choises
from .serializers import ProductSerializer, CategorySerializer, ChoisesSerializer, ProductListSerializer

# Create your views here.
class ProductsViewSet(views.APIView):
    authentication_classes = []
    permission_classes = [AllowAny,]
    def get(self, request):
        list_products = Products.objects.all() 
        serializer = ProductListSerializer(list_products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class ProductsManageViewSet(views.APIView):
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAdminUser,]
    
    def post(self, request):
        data = request.data
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.create(data=data)
            return Response({'message': 'creado correctamente'}, status=status.HTTP_201_CREATED)
        return Response({'erorr': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, slug):
        data = request.data
        try:
            product = Products.objects.get(slug=slug)
        except:
            return Response({'error': 'error'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = ProductSerializer(product, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'se a editado'}, status=status.HTTP_201_CREATED)
        return Response({'error': 'error'}, status=status.HTTP_400_BAD_REQUEST)
    
class PoductsDetailViewSet(views.APIView):
    authentication_classes = []
    permission_classes = [AllowAny,]
    def get(self, request, slug):
        try:
            product = Products.objects.get(slug=slug)
        except:
            return Response({'error': 'error'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class CategoryViewSet(views.APIView):
    authentication_classes = []
    permission_classes = [AllowAny,]
    def get(self, request):
        list_category = Category.objects.all()
        serializer = CategorySerializer(list_category, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class CategoryManageViewSet(views.APIView):
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAdminUser,]
    def post(self, request):
        data = request.data
        serializer = CategorySerializer(data=data)
        if serializer.is_valid():
            serializer.create(data=data)
            return Response({'message': 'creado correctamente'}, status=status.HTTP_201_CREATED)
        return Response({'erorr': 'bad request'}, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, slug):
        data = request.data
        try:
            category = Category.objects.get(slug=slug)
        except:
            return Response({'error': 'error'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = CategorySerializer(category, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'se a editado'}, status=status.HTTP_201_CREATED)
        return Response({'error': 'error'}, status=status.HTTP_400_BAD_REQUEST)

class CategoryDetailViewSet(views.APIView):
    authentication_classes = []
    permission_classes = [AllowAny,]
    def get(self, request, slug):
        try:
            category = Category.objects.get(slug=slug)
            products = Products.objects.filter(category=category)
        except:
            return Response({'error': 'error'}, status=status.HTTP_400_BAD_REQUEST)
        serializerProducts = ProductSerializer(products, many=True)
        serializerCategory = CategorySerializer(category)
        return Response({'category': serializerCategory.data, 'products': serializerProducts.data}, status=status.HTTP_200_OK)
    


class ChoisesViewSet(views.APIView):
    authentication_classes = []
    permission_classes = [AllowAny,]
    def get(self, request):
        list_choises = Choises.objects.all()
        serializer = ChoisesSerializer(list_choises, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class ChoisesManageViewSet(views.APIView):
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAdminUser,]
    def post(self, request):
        data = request.data
        serializer = ChoisesSerializer(data=data)
        if serializer.is_valid():
            serializer.create(data=data)
            return Response({'message': 'creado correctamente'}, status=status.HTTP_201_CREATED)
        return Response({'erorr': 'bad request'}, status=status.HTTP_400_BAD_REQUEST)