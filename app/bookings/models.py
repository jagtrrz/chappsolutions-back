from django.db import models

from app.contact.models import Contact
from app.rooms.models import Rooms
from app.core.models import Audit


class Bookings(Audit):
    """ Stores reservation information """
    check_in = models.DateField(help_text="Hotel check-in day", null=False)
    check_out = models.DateField(help_text="Hotel check-out day", null=False)
    number_of_guests = models.IntegerField(help_text="Number of guests in the reservation", null=False)
    total_price = models.FloatField(help_text="Total price of the booking", null=False)
    locator = models.CharField(help_text="Unique reserve locator", max_length=10, null=False, unique=True)
    room_number = models.CharField(max_length=10, blank=True, null=True)
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE, null=True)
    contact = models.OneToOneField(Contact, on_delete=models.CASCADE)

    class Meta:
        indexes = [
            models.Index(fields=['id']),
            models.Index(fields=['room', 'contact']),
        ]

    def __str__(self):
        return self.locator

