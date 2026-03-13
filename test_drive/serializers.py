from rest_framework import serializers
from .models import TestDrive

class TestDriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestDrive
        fields = ['id', 'product', 'dealer', 'name', 'email', 'phone', 'date', 'created_at']

    def validate_phone(self, value):
        if not value.startswith("+996"):
            value = "+996" + value.lstrip("0")
        return value