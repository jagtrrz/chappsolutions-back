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
        if type(booking.check_out) is str and type(booking.check_in) is str:
            return None
        else:
            total_nights = (booking.check_out - booking.check_in).days
            return total_nights
