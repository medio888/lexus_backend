from rest_framework import generics
from .models import TestDrive
from .serializers import TestDriveSerializer


class TestDriveListCreateView(generics.ListCreateAPIView):
    queryset = TestDrive.objects.all()
    serializer_class = TestDriveSerializer


class TestDriveDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TestDrive.objects.all()
    serializer_class = TestDriveSerializer