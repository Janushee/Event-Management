from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'name', 'date', 'total_tickets', 'tickets_sold']
        read_only_fields = ['id', 'tickets_sold']

class TicketPurchaseSerializer(serializers.Serializer):
    quantity = serializers.IntegerField(min_value=1, required=True)

    def validate_quantity(self, value):
        if value <= 0:
            raise serializers.ValidationError("Quantity must be greater than zero.")
        return value