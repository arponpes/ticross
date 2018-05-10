from django.test import TestCase
from core.models import Project, ActivityJournal
from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework import status
from core.factories import ProjectFactory, UserFactory, ActivityJournalFactory, RegistryFactory
import datetime as dt
import pytest


@pytest.mark.django_db
def test_calculate_one_activity():
    project = ProjectFactory()
    user = UserFactory()
    activity_journal = ActivityJournal.objects.create(
        project=project,
        user=user,
        time_lapse=10
    )

    total_time = project.time_calculator(user=user)

    assert str(dt.timedelta(seconds=10)) == total_time


@pytest.mark.django_db
def test_close_activity():
    start_date = timezone.now()-timezone.timedelta(hours=3)
    activity_journal = ActivityJournalFactory(
        start=start_date,
    )
    activity_journal.close_activity()
    assert activity_journal.time_lapse == timezone.timedelta(
        hours=3).total_seconds()


@pytest.mark.django_db
def test_check_out():
    registry = RegistryFactory()
    registry.check_out()
    assert registry.end != None
