from django.db.models import Q, F
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from datetime import datetime

from app.bookings.models import Bookings
from app.rooms.models import Rooms
from app.rooms.serializer import RoomsSerializer, RoomsDetailsSerializer


class RoomsViewSet(viewsets.ModelViewSet):
    queryset = Rooms.objects.all()
    serializer_class = RoomsSerializer

    def list(self, request, *args, **kwargs):
        guest = request.query_params.get('number_of_guest', None)
        check_in = request.query_params.get('check_in', None)
        check_out = request.query_params.get('check_out', None)

        bookings = Bookings.objects.filter(Q(check_in__range=(check_in, check_out)) |
                                           Q(check_out__range=(check_in, check_out))).all()

        rooms_ids = []
        if bookings.count() > 0:
            """Thats means that we have booking rooms in this dates"""
            for booking in bookings:
                rooms_ids.append(booking.room_id)

        rooms_available = self.queryset.filter(max_guest__gte=guest).exclude(Q(id__in=rooms_ids) |
                                                                             Q(stock_reserves=F('stock')))

        if rooms_available.count() == 0:
            raise ValidationError("No quedan habitaciones disponibles para estas fechas y para este número de personas")

        _check_in = datetime.strptime(check_in, '%Y-%m-%d')
        _check_out = datetime.strptime(check_out, '%Y-%m-%d')

        context = {
            'total_nights': (_check_out - _check_in).days,
            'check_in': datetime.strftime(_check_in, "%d-%m-%Y"),
            'check_out': datetime.strftime(_check_out, "%d-%m-%Y"),
            'number_of_guests': guest
        }

        serializer = RoomsDetailsSerializer(rooms_available, many=True, context=context).data

        return Response(serializer)

