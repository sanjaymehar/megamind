from rest_framework import serializers
from .models import BookingType


class PriceCalculationSerializer(serializers.Serializer):
    booking_type = serializers.PrimaryKeyRelatedField(queryset=BookingType.objects.all())
    number_of_days = serializers.IntegerField()
    number_of_adults = serializers.IntegerField()
    number_of_children = serializers.IntegerField()
