
import uuid
from django.db.models import Q
from django.db import transaction
from django.forms import ValidationError
from rest_framework.response import Response
from rest_framework import viewsets

from app.bookings.models import Bookings
from app.bookings.serializer import BookingSerializer
from app.contact.models import Contact
from app.rooms.models import Rooms


class BookingsViewSet(viewsets.ModelViewSet):
    queryset = Bookings.objects.all().order_by('-creation_date')
    serializer_class = BookingSerializer

    @transaction.atomic()
    def create(self, request, *args, **kwargs):
        data = request.data

        new_contact = Contact.objects.create(**data['contact'])
        room = Rooms.objects.filter(id=data['room']).first()

        """Check if room is booking this dates"""
        room_booking = Bookings.objects.filter(room=room).filter(Q(check_in__range=(data['check_in'], data['check_out'])) |
                                           Q(check_out__range=(data['check_in'], data['check_out']))).first()
        if room_booking is not None:
            raise ValidationError('You cannot continue with the reservation. This room is booked on these dates')

        data['room'] = room
        data['contact'] = new_contact
        data['locator'] = uuid.uuid4().hex[:8].upper()

        new_booking = Bookings.objects.create(**data)

        """Update room reserves"""
        room.stock_reserves = room.stock_reserves + 1
        room.save(update_fields=['stock_reserves'])

        serializer = self.serializer_class(new_booking)

        return Response(status=200, data=serializer.data)

    def list(self, request, *args, **kwargs):
        
        if self.queryset.count() == 0:
            raise ValidationError("No booking at the moment")

        page = self.paginate_queryset(self.queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)


