from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    director = models.CharField(max_length=100, null=True, blank=True)
    genere = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name
