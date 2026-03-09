from django.contrib import admin
from .models import TestDrive


@admin.register(TestDrive)
class TestDriveAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "car", "date", "created_at")
    search_fields = ("name", "phone")