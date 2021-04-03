from rest_framework import serializers,generics
from .models import Species, Refined_Sighting, Location ,Raw_Sighting
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username','email','password')
        extra_kwargs = {'password':{'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        return user

#Login Serializer
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and  user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")



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

class Raw_Sighting_Serializer(serializers.ModelSerializer):
    class Meta:
        fields='__all__'
        model=Raw_Sighting