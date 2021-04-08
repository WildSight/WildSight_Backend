from django.shortcuts import render
from .models import Species, Refined_Sighting, Location, Raw_Sighting
from .serializers import SpeciesSerializer, Refined_Sighting_Serializer, Raw_Sighting_Serializer, LocationSerializer, UserSerializer, RegisterSerializer, LoginSerializer
from rest_framework import generics, permissions, filters, status
from rest_framework.response import Response
from knox.models import AuthToken
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.parsers import MultiPartParser, FormParser


# Create your views here.

class Species_list(generics.ListAPIView):
    queryset=Species.objects.all()
    serializer_class=SpeciesSerializer
    filter_backends=[filters.SearchFilter]
    search_fields=['common_name']

class Locations_list(generics.ListAPIView):
    #queryset=Location.objects.all()
    serializer_class=LocationSerializer

    def get_queryset(self):
        queryset=Location.objects.all()
        latitude=(self.request.query_params.get('lat'))
        longitude=(self.request.query_params.get('long'))
        if latitude is None and longitude is None:
            return queryset
        queryset=Location.objects.filter(y_coordinate_start__lt=latitude, y_coordinate_end__gte = latitude, x_coordinate_start__lt=longitude, x_coordinate_end__gte=longitude)
        return queryset

class Refined_Sightings_list(generics.ListAPIView):
    queryset=Refined_Sighting.objects.all()
    serializer_class=Refined_Sighting_Serializer

class Species_element(generics.RetrieveAPIView):
    queryset=Species.objects.all()
    serializer_class=SpeciesSerializer

class Refined_Sightings_Species_list(generics.ListAPIView):
    serializer_class=Refined_Sighting_Serializer

    def get_queryset(self):
        queryset=Refined_Sighting.objects.all()
        sp=self.request.query_params.get('sp')
        time=self.request.query_params.get('time')
        if time is None:
            return queryset.filter(Species=sp)
        return queryset.filter(Species=sp, time_period=time)
    

class Refined_Sightings_Locations_list(generics.ListAPIView):
    serializer_class=Refined_Sighting_Serializer

    def get_queryset(self):
        queryset=Refined_Sighting.objects.all()
        loc=self.request.query_params.get('loc')
        time=self.request.query_params.get('time')
        if time is None:
            return queryset.filter(Location=loc)
        return queryset.filter(Location=loc, time_period=time)

class Raw_Sighting_Input(generics.ListCreateAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    parser_classes = [MultiPartParser, FormParser]
    
    def get_serializer(self, *args, **kwargs):
        # leave this intact
        serializer_class = self.get_serializer_class()
        kwargs["context"] = self.get_serializer_context()

        """
        Intercept the request and see if it needs tweaking
        """
        
        # Copy and manipulate the request
        draft_request_data = self.request.data.copy()
        draft_request_data["user"] = User.objects.get(username=draft_request_data["user"]).pk
        draft_request_data["species"] = Species.objects.get(common_name = draft_request_data["species"]).id
        kwargs["data"] = draft_request_data
        return serializer_class(*args, **kwargs)

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
    authentication_classes = [BasicAuthentication]

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


class Ratification_List(generics.ListAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class=Raw_Sighting_Serializer

    def get_queryset(self):
        queryset=Raw_Sighting.objects.filter(credible=False)
        user=self.request.user
        queryset=queryset.exclude(user=user)
        num=self.request.query_params.get('num')
        if num is not None:
            return queryset[0:num]
        return queryset

# class vote(generics.UpdateAPIView):
#     permission_classes = [
#         permissions.IsAuthenticated,
#     ]
#     serializer_class=Raw_Sighting_Serializer

#     def patch(self):
#         votestr=self.request.query_params.get('vote')
#         queryset=Raw_Sighting.objects.all()
#         if votestr=='up':
#             queryset.upvotes+=1
#         elif votestr=='down':
#             queryset.downvotes+=1
#         if queryset.upvotes+queryset.downvotes>=10:
#             if queryset.upvotes/queryset.downvotes >= 0.7:
