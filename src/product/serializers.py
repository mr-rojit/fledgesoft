from rest_framework import serializers
from product.models import Product, Category

class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
    

class ProductModelSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(write_only=True)
    category = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Product
        exclude = 'is_deleted', 'status', 'created_at', 'updated_at'


class ProductDetailModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = 'is_deleted', 'status', 'created_at', 'updated_at'

    
class CategortWithProductSerializer(serializers.ModelSerializer):
    products = ProductModelSerializer(many=True, read_only=True, source="product_set")

    class Meta:
        model = Category
        fields = 'id', 'name', 'description', 'products'

