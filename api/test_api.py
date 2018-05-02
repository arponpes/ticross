from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import RequestsClient
from rest_framework.reverse import reverse
from rest_framework.authtoken.models import Token


def test_request(admin_client):
    response = admin_client.get(reverse('api:project-list'))
    assert response.status_code == 200


def test_create_project(admin_client):
    user = User.objects.create(username='user')
    data = {
        'user': [user.pk],
        'project_name': 'project 01',
        'description': 'Esto es una descripcion',
    }
    response = admin_client.post('/api/projects/', data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
