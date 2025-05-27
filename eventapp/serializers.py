# eventapp/serializers.py

from rest_framework import serializers
from .models import Event
from .models import ContactMessage


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__' 

class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ['id', 'name', 'email', 'message', 'created_at']
