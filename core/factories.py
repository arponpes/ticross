import factory
from .models import Project, ActivityJournal, Registry
from django.contrib.auth.models import User
from django.utils import timezone
import datetime as dt


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('user_name')
    password = factory.Faker('password')
    @classmethod
    def _prepare(cls, create, **kwargs):
        if 'password' in kwargs:
            password = kwargs.pop('password')
        user = super(UserFactory, cls)._prepare(create, **kwargs)
        user.set_password(password)
        if create:
            user.save()
        return user


class ProjectFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Project

    project_name = factory.Faker('last_name', locale='en_US')
    description = factory.Faker('text')


class ActivityJournalFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ActivityJournal

    project = factory.SubFactory(ProjectFactory)
    user = factory.SubFactory(UserFactory)


class RegistryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Registry

    start = factory.LazyFunction(timezone.now)
    user = factory.SubFactory(UserFactory)
