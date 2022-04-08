from django.db import models


class Audit(models.Model):
    """ Model to save dates of creation, edition and users with the idea of inheriting in the rest of the models. """
    active = models.BooleanField(default=True)
    creation_date = models.DateTimeField(auto_now_add=True, null=True)
    created_by = models.CharField(max_length=100, blank=True, null=True, default=None,
                                  help_text='User who create the record')
    update_date = models.DateTimeField(auto_now=True, null=True)
    update_by = models.CharField(max_length=100, blank=True, null=True, default=None,
                                 help_text='User who update the record')

    class Meta:
        abstract = True
