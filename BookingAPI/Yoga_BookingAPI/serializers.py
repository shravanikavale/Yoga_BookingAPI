from rest_framework import serializers
from .models import FitnessClass, Bookings

class FitnessClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = FitnessClass
        fields = '__all__'

class BookingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookings
        fields = '__all__'

    def validate(self, data):
        if Bookings.objects.filter(
            fitness_class=data['fitness_class'],
            client_email=data['client_email']
        ).exists():
            raise serializers.ValidationError("You have already booked this class.")
        if data['fitness_class'].available_slots < 1:
            raise serializers.ValidationError("No slots available.")
        return data
