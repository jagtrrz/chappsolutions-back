import uuid

from django.db import transaction
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
        #TODO MIRAR SI LAS FECHAS Y EL TIPO DE HAB ESTA LIBRE
        room = Rooms.objects.filter(id=data['room']).first()
        new_contact = Contact.objects.create(**data['contact'])

        data['room'] = room
        data['contact'] = new_contact
        data['locator'] = uuid.uuid4().hex[:8].upper()

        new_booking = Bookings.objects.create(**data)

        print("ffffffffffffffffffffff", new_booking)

        serializer = self.serializer_class(new_booking)

        return Response(status=200, data=serializer.data)

    def list(self, request, *args, **kwargs):

        page = self.paginate_queryset(self.queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)


