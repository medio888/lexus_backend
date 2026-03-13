from rest_framework import serializers
from .models import Dealer


class DealerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dealer
        fields = [
            "id",
            "first_name",
            "last_name",
            "birth_year",
            "has_driver_license"
        ]