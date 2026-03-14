from rest_framework import serializers
from .models import Dealer


class DealerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dealer
        fields = [
            'id',
            'name',
            'email',
            'phone',
            'address',
        ]