from rest_framework import serializers
from .models import Species, Refined_Sighting, Location

class SpeciesSerializer(serializers.ModelSerializer):
    class Meta:
        fields=(
            'id',
            'common_name',
            'scientific_name',
        )
        model=Species

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        fields=(
            'id',
            'x_coordinate_start',
            'x_coordinate_end',
            'y_coordinate_start',
            'y_coordinate_end',
        )
        model=Location

class Refined_Sighting_Serializer(serializers.ModelSerializer):
    class Meta:
        fields=(
            'id',
            'Species',
            'Location',
            'time_period',
            'Count',
            'Number_of_sightings',
        )
        model=Refined_Sighting