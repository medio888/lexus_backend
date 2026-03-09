from django.db import models
from api.models import Products 

class TestDrive(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    date = models.DateTimeField()
    car = models.ForeignKey(Products, on_delete=models.CASCADE, related_name="test_drives")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.car}"