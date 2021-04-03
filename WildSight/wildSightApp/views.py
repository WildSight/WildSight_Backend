from django.shortcuts import render
from .models import Species, Refined_Sighting, Location, Raw_Sighting
from .serializers import SpeciesSerializer, Refined_Sighting_Serializer, Raw_Sighting_Serializer, LocationSerializer, UserSerializer, RegisterSerializer, LoginSerializer
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from rest_framework.views import APIView
from rest_framework.parsers import JSONParse

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

class Raw_Sighting_Input(generics.ListCreateAPIView):
    serializer_class = Raw_Sighting_Serializer

    queryset = Raw_Sighting.objects.all()
    
   

#Register API

class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user,context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })

# Login API
class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user": UserSerializer(user,context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })

#Get user API
class UserAPI(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
