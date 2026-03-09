from rest_framework.routers import DefaultRouter
from .views import TestDriveViewSet

router = DefaultRouter()
router.register('testdrive', TestDriveViewSet)