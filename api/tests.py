from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import RequestsClient
from rest_framework.reverse import reverse
from rest_framework.authtoken.models import Token


class RequestTests(APITestCase):

    def test_request(self):
        response = self.client.get(reverse('api:project-list'))
        assert response.status_code == 403



class ProjectTest(APITestCase):

    def test_create_project(self):
        
        user = User.objects.create(username='admin')
        self.client.force_authenticate(user=user)
        data = {
            'user': [user.pk],
            'project_name': 'project 01',
            'description': 'Esto es una descripcion',
        }
        response = self.client.post('/api/projects/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.data)
