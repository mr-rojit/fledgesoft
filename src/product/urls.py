from django.urls import path, include
from .views import CategoryModelViewSet, ProductListCreateAPIView, ProductDetailAPIView, CategoryProductView

app_name = "product"

from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register("categories", CategoryModelViewSet, basename="categories")

urlpatterns = [
    path('products/<int:pk>/', ProductDetailAPIView.as_view(), name="product-detail"),
    path('products/', ProductListCreateAPIView.as_view(), name="product-list-create"),
    path('category-products/', CategoryProductView.as_view(), name="category-product-list"),
    path("", include(router.urls)),
]