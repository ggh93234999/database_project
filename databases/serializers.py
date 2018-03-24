from rest_framework import serializers
from databases.models import *

class DepartmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = '__all__'

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

class TeamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teams
        fields = '__all__'

class TeammembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teammembers
        fields = '__all__'

class SetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sets
        fields = '__all__'

class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = '__all__'

class SeteventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setevents
        fields = '__all__'

class MatchesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matches
        fields = '__all__'

class MatchteamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matchteams
        fields = '__all__'

class RegistrationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registrations
        fields = '__all__'

