from django.shortcuts import render
from rest_framework import viewsets, status, permissions
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from core.models import *
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from core.serializers import *

# Create your views here.

class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    
class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers

class ImageView(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializers

class OrderView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializers

class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        # Authenticate user
        user = User.objects.get(email = email,password = password)
        
        if user is not None:
            # If authentication is successful, serialize user data
            serializer = UserSerializers(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            # If authentication fails, return an unauthorized response
            return Response({"message": "Invalid email or password."}, status=status.HTTP_401_UNAUTHORIZED)
        
class OrderDetailView(APIView):
    def post(self, request):
        orderno = request.data.get('orderno')
        order = Order.objects.get(orderno = orderno)
        
        if order is not None:
            # serializer = UserSerializers(user)
            serializer = OrderSerializers(order)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Invalid Order No."}, status=status.HTTP_404_NOT_FOUND)
        
class OrderbyUser(APIView):
    def post(self, request):
        user = request.data.get('user')
        order = Order.objects.filter(user = user)
        
        if order.exists():
            # serializer = UserSerializers(user)
            serializer = OrderSerializers(order,many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Invalid Order No."}, status=status.HTTP_404_NOT_FOUND)
