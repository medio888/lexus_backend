from django.contrib import admin
from .models import TestDrive

@admin.register(TestDrive)
class TestDriveAdmin(admin.ModelAdmin):
    pass