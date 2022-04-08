from django.db import models
from app.core.models import Audit


class Contact(Audit):
    """ Stores a contact's information for reservations or other purposes """
    name = models.CharField(max_length=150, null=False)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=25, null=False)

    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]

    def __str__(self):
        return self.name
