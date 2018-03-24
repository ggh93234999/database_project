from django.shortcuts import render

from databases.models import *
from databases.serializers import *

from rest_framework import viewsets

# Create your views here.

class DepartmentsViewSet(viewsets.ModelViewSet):
    queryset = Departments.objects.all()
    serializer_class = DepartmentsSerializer

class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

class TeamsViewSet(viewsets.ModelViewSet):
    queryset = Teams.objects.all()
    serializer_class = TeamsSerializer

class TeammembersViewSet(viewsets.ModelViewSet):
    queryset = Teammembers.objects.all()
    serializer_class = TeammembersSerializer

class SetsViewSet(viewsets.ModelViewSet):
    queryset = Sets.objects.all()
    serializer_class = SetsSerializer

class EventsViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer

class SeteventsViewSet(viewsets.ModelViewSet):
    queryset = Setevents.objects.all()
    serializer_class = SeteventsSerializer

class MatchesViewSet(viewsets.ModelViewSet):
    queryset = Matches.objects.all()
    serializer_class = MatchesSerializer

class MatchteamsViewSet(viewsets.ModelViewSet):
    queryset = Matchteams.objects.all()
    serializer_class = MatchteamsSerializer

class RegistrationsViewSet(viewsets.ModelViewSet):
    queryset = Registrations.objects.all()
    serializer_class = RegistrationsSerializer

