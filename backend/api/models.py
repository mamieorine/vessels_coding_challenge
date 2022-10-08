from django.db import models


class Vessel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False, blank=True)
    lat = models.FloatField(blank=True)
    lng = models.FloatField(blank=True)
    address = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name
