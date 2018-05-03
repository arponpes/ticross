from django import forms
from .views import LoginWithCheckIn
from core.factories import UserFactory
from django.test import Client
import pytest


@pytest.mark.django_db
def test_form_login(rf):
    user = UserFactory()
    request = rf.post('accounts/login/',{'username': user.username, 'password': user.password})
    response = user.login()
    assert response.status_code == 200
