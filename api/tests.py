from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import RequestsClient
from rest_framework.reverse import reverse


class RequestTests(APITestCase):

    def test_request(self):
        response = self.client.get(reverse('api:project-list'))
        assert response.status_code == 403
