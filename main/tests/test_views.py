from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import json

class MainTestsViews(APITestCase):
    def test_customer_list_view(self):
        url = 'main:customer-list'
        response = self.client.get(reverse(url))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
