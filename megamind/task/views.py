from rest_framework import generics
from rest_framework.response import Response
from .models import BookingType
from .serializer import PriceCalculationSerializer
from .utils import calculate_price


class CalculatePriceAPIView(generics.CreateAPIView):
    serializer_class = PriceCalculationSerializer

    def create(self, request, *args, **kwargs):
        booking_data = request.data
        booking_type_id = booking_data.get('booking_type')
        num_days = int(booking_data.get('number_of_days'))
        num_adults = int(booking_data.get('number_of_adults'))
        num_children = int(booking_data.get('number_of_children'))

        try:
            booking_type = BookingType.objects.get(pk=booking_type_id)
        except BookingType.DoesNotExist:
            return Response({'error': 'Booking type not found'}, status=400)

        calculated_price = calculate_price(booking_type, num_days, num_adults, num_children)

        response_data = {
            'calculated_price': calculated_price
        }

        return Response(response_data)
