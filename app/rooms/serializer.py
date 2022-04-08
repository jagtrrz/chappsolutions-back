import uuid

from rest_framework import serializers

from app.rooms.models import Rooms


class RoomsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Rooms
        fields = '__all__'


class RoomsDetailsSerializer(serializers.ModelSerializer):
    total_nights = serializers.SerializerMethodField()
    total_price = serializers.SerializerMethodField()
    total_available = serializers.SerializerMethodField()
    check_in = serializers.SerializerMethodField()
    check_out = serializers.SerializerMethodField()
    number_of_guests = serializers.SerializerMethodField()

    def get_total_nights(self, room):
        total_nigths = self.context.get('total_nights')
        return total_nigths

    def get_total_price(self, room):
        total_nigths = self.context.get('total_nights')
        total_price = total_nigths * room.price_per_night
        return total_price

    def get_total_available(self, room):
        return room.stock - room.stock_reserves

    def get_check_in(self, room):
        check_in = self.context.get('check_in')
        return check_in

    def get_check_out(self, room):
        check_out = self.context.get('check_out')
        return check_out

    def get_number_of_guests(self, room):
        number_of_guests = self.context.get('number_of_guests')
        return number_of_guests

    class Meta:
        model = Rooms
        fields = '__all__'

