from rest_framework import viewsets
from .models import TestDrive
from .serializers import TestDriveSerializer
from django.core.mail import send_mail
from django.conf import settings

class TestDriveViewSet(viewsets.ModelViewSet):
    queryset = TestDrive.objects.all()
    serializer_class = TestDriveSerializer

    def perform_create(self, serializer):
        testdrive = serializer.save()
        subject = f"Новая заявка на тест-драйв от {testdrive.name}"
        message = f"""
Имя: {testdrive.name}
Телефон: +996{testdrive.phone}
Email: {testdrive.email}
Продукт: {testdrive.product}
Дилер: {testdrive.dealer}
Дата заявки: {testdrive.date}
"""
        recipient_list = [testdrive.dealer.email]
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list, fail_silently=False)