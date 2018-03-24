from django.db import models

# Create your models here.


class Departments(models.Model):
    name         = models.CharField(max_length = 20)
    grade        = models.DecimalField(max_digits = 3, decimal_places = 0)
    classtype    = models.CharField(max_length = 40)

class Users(models.Model):
    name         = models.CharField(max_length = 20)
    phonenumber  = models.CharField(max_length = 15)
    gender       = models.CharField(max_length = 5)
    email        = models.CharField(max_length = 40)
    departmentid = models.ForeignKey(Departments, on_delete = models.DO_NOTHING)
	
class Teams(models.Model):
    name         = models.CharField(max_length = 20)
    
class Teammembers(models.Model):
    teamid       = models.ForeignKey(Teams, on_delete = models.DO_NOTHING)
    userid       = models.ForeignKey(Users, on_delete = models.DO_NOTHING)

class Sets(models.Model):
    name         = models.CharField(max_length = 100)

class Events(models.Model):
    name         = models.CharField(max_length = 100)
    maxnum       = models.DecimalField(max_digits = 3, decimal_places = 0)
    minnum       = models.DecimalField(max_digits = 3, decimal_places = 0)

class Setevents(models.Model):
    setid        = models.ForeignKey(Sets, on_delete = models.DO_NOTHING)
    eventid      = models.ForeignKey(Events, on_delete = models.DO_NOTHING)

class Matches(models.Model):
    eventid      = models.ForeignKey(Events, on_delete = models.DO_NOTHING)
    datetime     = models.DateTimeField()
    valid        = models.BooleanField()
    socre        = models.CharField(max_length = 100)

class Matchteams(models.Model):
    matchid      = models.ForeignKey(Matches, on_delete = models.DO_NOTHING)
    teamid       = models.ForeignKey(Teams, on_delete = models.DO_NOTHING)

class Registrations(models.Model):
    registertime = models.DateTimeField(auto_now = True)
    teamid       = models.ForeignKey(Teams, on_delete = models.DO_NOTHING)
    setid        = models.ForeignKey(Sets, on_delete = models.DO_NOTHING)
    eventid      = models.ForeignKey(Events, on_delete = models.DO_NOTHING)


