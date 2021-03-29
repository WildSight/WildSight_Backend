from django.shortcuts import render
from rest_framework import generics
from .models import Species, Refined_Sighting, Location
from .serializers import SpeciesSerializer, Refined_Sighting_Serializer, LocationSerializer

# Create your views here.

class Species_list(generics.ListAPIView):
    queryset=Species.objects.all()
    serializer_class=SpeciesSerializer

class Locations_list(generics.ListAPIView):
    queryset=Location.objects.all()
    serializer_class=LocationSerializer

class Refined_Sightings_list(generics.ListCreateAPIView):
    queryset=Refined_Sighting.objects.all()
    serializer_class=Refined_Sighting_Serializer

class Species_element(generics.RetrieveAPIView):
    queryset=Species.objects.all()
    serializer_class=SpeciesSerializer

class Refined_Sightings_Species_list(generics.RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        sp=self.kwargs['pk']
        return Refined_Sighting.objects.filter(Species=sp)
    serializer_class=Refined_Sighting_Serializer

class Refined_Sightings_Locations_list(generics.RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        return Refined_Sighting.objects.filter(Location=self.kwargs['pk'])
    serializer_class=Refined_Sighting_Serializer

