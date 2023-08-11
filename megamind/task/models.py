from django.db import models


class BookingType(models.Model):
    name = models.CharField(max_length=100)
    formula = models.CharField(max_length=200)

    def __str__(self):
        return self.name
