from rest_framework import serializers
from .models import Booking, Event
# eventapp/serializers.py

from rest_framework import serializers
from .models import Event
from .models import ContactMessage


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
<<<<<<< HEAD
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    event_name = serializers.CharField(source='event.name', read_only=True)

    class Meta:
        model = Booking
        fields = '__all__'
        read_only_fields = ['total_price']
    def create(self, validated_data):
        # Calculate total price based on ticket quantity and price per ticket
        validated_data['total_price'] = validated_data['ticket_quantity'] * validated_data['price_per_ticket']
        return super().create(validated_data)
=======
        fields = '__all__' 

class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ['id', 'name', 'email', 'message', 'created_at']
>>>>>>> 242627f525c96f0cf33a0494332c6fb0b9a1d423
