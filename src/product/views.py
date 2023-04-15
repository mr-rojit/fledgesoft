from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.response import Response
from product.serializers import ProductModelSerializer, ProductDetailModelSerializer,\
CategortWithProductSerializer, CategoryModelSerializer
from rest_framework.viewsets import ModelViewSet

from product.models import Product, Category

""" Category Viwes   """
class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer

    def destroy(self,*args, **kwargs):
        print('****************************************')
        return super().destroy(*args, **kwargs)


class CategoryProductView(ListAPIView):
    serializer_class = CategortWithProductSerializer
    queryset = Category.objects.all()


""" Product Views  """
class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.filter(is_deleted=False)
    serializer_class = ProductModelSerializer

    def post(self, request, *args, **kwargs):
        serializer = ProductModelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        category = serializer.validated_data.get('category_name', None)
        category , _ = Category.objects.get_or_create(name = category)
        del serializer.validated_data['category_name']
        product = Product.objects.create(category=category, **serializer.validated_data)
        return Response(product.pk, status=201)


class ProductDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductDetailModelSerializer
    queryset = Product.objects.all()
