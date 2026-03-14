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
Поступила новая заявка:

Имя: {testdrive.name}
Телефон: {testdrive.phone}
Email: {testdrive.email if testdrive.email else 'Не указан'}
Продукт: {testdrive.product}
Дилер: {testdrive.dealer}
Дата записи: {testdrive.date.strftime('%d.%m.%Y %H:%M')}
"""
        
        recipient_list = ['asanbekovmeder88@gmail.com'] 

        send_mail(
            subject, 
            message, 
            settings.DEFAULT_FROM_EMAIL, 
            recipient_list, 
            fail_silently=False
        )