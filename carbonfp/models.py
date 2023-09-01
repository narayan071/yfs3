from django.db import models

class CarbonFootprint(models.Model):
    motorcycle = models.BooleanField(default=False)
    q_motorcycle = models.FloatField(default=0.0)
    persons_motorcycle = models.IntegerField(default=0)
    car = models.BooleanField(default=False)
    q_car = models.FloatField(default=0.0)
    persons_car = models.IntegerField(default=0)
    bus = models.BooleanField(default=False)
    q_bus = models.FloatField(default=0.0)
    train = models.BooleanField(default=False)
    q_train = models.FloatField(default=0.0)
    plane = models.BooleanField(default=False)
    q_plane = models.IntegerField(default=0)
    ship = models.BooleanField(default=False)
    q_ship = models.IntegerField(default=0)

    # Add other fields as needed
