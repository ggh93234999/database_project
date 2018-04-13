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

#-------------- email sending test ----------------------

from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.http import HttpResponse

def SendmailViewSet(request):
    send_mail(
        'Subject',
        'Message',
        'Lin Hsiang <nctudatabase@gmail.com>',
        ['ggh93234999@gmail.com', 'ggh93234999@yahoo.com.tw']
    )
    return HttpResponse("Send successful!")


#-------------- after here is just for test ----------------------


from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

def Singup(request):
    
    if request.method == 'POST':
        try:
            uname = request.POST['username']
            upass = request.POST['password']
            umail = request.POST['email']
            print(uname,upass,umail)
            tmp_new_user = User.objects.create_user(uname, umail, upass)
            return HttpResponse("Create Successful")

        except:
            response = HttpResponse("Sothing Error")
            response.status_code = 400
            return response



