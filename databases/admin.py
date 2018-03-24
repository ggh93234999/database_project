from django.contrib import admin
from databases.models import *

# Register your models here.

admin.site.register(Departments)
admin.site.register(Users)
admin.site.register(Teams)
admin.site.register(Teammembers)
admin.site.register(Sets)
admin.site.register(Events)
admin.site.register(Setevents)
admin.site.register(Matches)
admin.site.register(Matchteams)
admin.site.register(Registrations)

