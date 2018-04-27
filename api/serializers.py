from rest_framework import serializers
from core.models import Project, ActivityJournal, Registry
from django.contrib.auth.models import User


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ('project_name', 'description', 'user')


class ActivityJournalSerializer(serializers.ModelSerializer):

    class Meta:
        model = ActivityJournal
        fields = ('user', 'project', 'start', 'end')


class RegistrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Registry
        fields = ('user', 'start', 'end')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'password')
