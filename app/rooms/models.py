from django.db import models

from app.core.models import Audit


class Rooms(Audit):
    """Stores the rooms with their price and stock"""
    room_type = models.CharField(help_text="Room type name",
                                 max_length=50, null=False, blank=False)
    price_per_night = models.FloatField(help_text="Price per night for each room", null=False)
    max_guest = models.IntegerField(help_text="Maximum number of guests per room", null=False)
    stock = models.IntegerField(help_text="Stock available for booking", null=False)
    stock_reserves = models.IntegerField(help_text="Total reserved stock units", null=True, default=0)
    image_url = models.CharField(help_text="Room image", max_length=225, null=True, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['id'])
        ]

    def __str__(self):
        return self.room_type
