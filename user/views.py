from rest_framework import viewsets
from .models import CustomUser
from .serializers import RegisterSerializer

class RegisterViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer