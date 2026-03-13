from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, SubCategoryViewSet, ProductsViewSet

router = DefaultRouter()
router.register('category', CategoryViewSet)
router.register('subcategory', SubCategoryViewSet)
router.register('products', ProductsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
