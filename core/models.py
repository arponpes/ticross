from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime


class Project(models.Model):
    user = models.ManyToManyField('auth.User')
    project_name = models.CharField(max_length=150)
    description = models.TextField()

    def time_calculator(self, user):
        timers = self.activityjournal_set.filter(
            user=user, project=self).values_list('time_lapse')
        total_time = 0
        for time in timers:
            if time[0] != None:
                total_time += time[0]
        
        return str(datetime.timedelta(seconds=total_time))

    def __str__(self):
        return self.project_name


class ActivityJournal(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    start = models.DateTimeField(default=datetime.datetime.now())
    end = models.DateTimeField(blank=True, null=True)
    time_lapse = models.IntegerField(blank=True, null=True)

    def close_activity(self):
        self.end = timezone.now()
        diff = self.end - self.start
        self.time_lapse = int(diff.total_seconds())
        self.save()

    def __str__(self):
        return 'Usuario: {}, Projecto: {}'.format(self.user, self.project)


class Registry(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    start = models.DateTimeField(default=datetime.datetime.now())
    end = models.DateTimeField(blank=True, null=True)

    def total_worked_today(self):
        
        return timezone.now() - self.start

    def __str__(self):
        return 'Usuario: {}, Hora de entrada: {}'.format(self.user, self.start)
