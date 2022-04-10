from rest_framework import serializers

from app.bookings.models import Bookings
from app.contact.serializer import ContactSerializer


class BookingSerializer(serializers.ModelSerializer):
    contact = ContactSerializer()
    room_type = serializers.SlugRelatedField(source='room', slug_field='room_type', read_only=True)
    total_nights = serializers.SerializerMethodField()

    class Meta:
        model = Bookings
        fields = '__all__'

    def get_total_nights(self, booking):
        total_nights = (booking.check_out - booking.check_in).days
        return total_nights
