from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, SubCategoryViewSet

router = DefaultRouter()
router.register('category', CategoryViewSet)
router.register('subcategory', SubCategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
