"""PE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from databases import views
from rest_framework_jwt.views import obtain_jwt_token

router = DefaultRouter()
router.register(r'Departments',views.DepartmentsViewSet)
router.register(r'Users',views.UsersViewSet)
router.register(r'Teams',views.TeamsViewSet)
router.register(r'Teammembers',views.TeammembersViewSet)
router.register(r'Sets',views.SetsViewSet)
router.register(r'Events',views.EventsViewSet)
router.register(r'Setevents',views.SeteventsViewSet)
router.register(r'Matches',views.MatchesViewSet)
router.register(r'Matchteams',views.MatchteamsViewSet)
router.register(r'Registrations',views.RegistrationsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('send/',views.SendmailViewSet),
    path(r'api-token-auth/',obtain_jwt_token),
    path('signup/',views.Singup),
#    path('restricted/', views.RestrictedView.as_view()),

]
