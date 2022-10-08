from rest_framework import serializers
from .models import Vessel


class VesselSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vessel
        fields = ["id", "name", "lat", "lng", "address"]
