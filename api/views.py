from rest_framework import viewsets
from .serializers import ProjectSerializer, ActivityJournalSerializer, RegistrySerializer, UserSerializer
from core.models import Project, ActivityJournal, Registry
from django.contrib.auth.models import User


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ActivityJournalViewSet(viewsets.ModelViewSet):
    queryset = ActivityJournal.objects.all()
    serializer_class = ActivityJournalSerializer


class RegistryViewSet(viewsets.ModelViewSet):
    queryset = Registry.objects.all()
    serializer_class = RegistrySerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
