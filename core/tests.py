from django.test import TestCase
from core.models import Project, ActivityJournal
from django.contrib.auth.models import User
from django.utils import timezone
from core.factories import ProjectFactory, UserFactory, ActivityJournalFactory, RegistryFactory
import datetime as dt


class TimeCalculator(TestCase):

    def test_calculate_one_activity(self):
        project = ProjectFactory()
        user = UserFactory()
        activity_journal = ActivityJournal.objects.create(
            project=project,
            user=user,
            time_lapse=10
        )

        total_time = project.time_calculator(user=user)

        self.assertEqual(str(dt.timedelta(seconds=10)), total_time)


class ActivityJournalModelTest(TestCase):

    def test_close_activity(self):
        start_date = timezone.now()-timezone.timedelta(hours=3)
        activity_journal = ActivityJournalFactory(
            start=start_date,
        )

        activity_journal.close_activity()

        self.assertEqual(activity_journal.time_lapse,
                         timezone.timedelta(hours=3).total_seconds())

        
