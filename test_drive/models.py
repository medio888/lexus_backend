from django.db import models
from api.models import Products 

class TestDrive(models.Model):
    name = models.CharField(verbose_name="Name", max_length=100)
    phone = models.CharField(verbose_name="Phone", max_length=20)
    date = models.DateTimeField(verbose_name="Date")
    car = models.ForeignKey(Products, on_delete=models.CASCADE, related_name="test_drives")
    email = models.EmailField(verbose_name="Email", null=False, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.car} - {self.email}"