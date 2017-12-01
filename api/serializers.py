from rest_framework import serializers
from api.models import Meeting, When, Location

class WhenSerializer(serializers.ModelSerializer):
    class Meta:
        model = When
        fields = ('day', 'time', 'duration')

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        feilds = ('country', 'city', 'street')

class MeetingSerializer(serializers.ModelSerializer):
    when = WhenSerializer(many=False)
    location = LocationSerializer(many=False)
    class Meta:
        model = Meeting
        fields = ('name', 'description', 'adress', 'when', 'location' ,"pk") #'country', 'city',