from rest_framework import serializers
from core.models import *

class ImageSerializers(serializers.ModelSerializer):
    id= serializers.ReadOnlyField()
    class Meta:
        model= Image
        fields='__all__'

class ProductSerializers(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    category_name = serializers.CharField(source='categroy.name',read_only=True)
    # images = ImageSerializers(many=True)
    class Meta:
        model=Product
        fields=['id','name','slug','price','oldPrice','category_name','category','info','rating','image','images']

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'phone', 'name'] 

class CategorySerializers(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model=Category
        fields='__all__'

class OrderSerializers(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model=Order
        fields='__all__'