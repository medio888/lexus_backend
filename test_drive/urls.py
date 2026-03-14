from rest_framework import routers
from .views import TestDriveViewSet

router = routers.DefaultRouter()
router.register('test_drives', TestDriveViewSet)