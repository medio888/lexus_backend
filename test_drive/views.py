from rest_framework import viewsets
from .models import TestDrive
from .serializers import TestDriveSerializer

class TestDriveViewSet(viewsets.ModelViewSet):
    queryset = TestDrive.objects.all()
    serializer_class = TestDriveSerializer