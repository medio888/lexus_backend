from django.contrib import admin
from .models import Dealer


@admin.register(Dealer)
class DealerAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
        "birth_year",
        "has_driver_license"
    )