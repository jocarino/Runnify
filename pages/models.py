from django.db import models
from django.contrib.postgres.fields import JSONField

class Coordinates(models.Model):
    """Model representing a route coordinate generated (e.g. Science Fiction, Non Fiction)."""
    coordinates = JSONField()

    def __str__(self):
        """String for representing the Coordinates objects"""
        return self.coordinates

class RouteRequest(models.Model):
    running_distance = models.FloatField(...)
    user_location = models.CharField(max_length=8000)