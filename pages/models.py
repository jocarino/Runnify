from django.db import models

class Coordinates(models.Model):
    """Model representing a book genre (e.g. Science Fiction, Non Fiction)."""
    coordinates = models.TextField(
        null=True,
        help_text="Enter a list of coords [[latitude, longitude],...]"
        )

    def __str__(self):
        """String for representing the Coordinates objects"""
        return self.coordinates
