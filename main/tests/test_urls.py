from rest_framework.test import APITestCase
from rest_framework import status
from ..models import Customer, Order
from django.urls import reverse
import datetime

# Intergration tests 
class CustomerAPITest(APITestCase):
    def setUp(self):
        Customer.objects.create(name='branson', code='fdjf2')

    def test_customers_list(self):
        url = reverse('main:customer-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_customer(self):
        url = reverse('main:customer-list')
        response = self.client.post(url,{'name':'branson', 'code':'jfjfd'} )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_customer_detail(self):
        url = reverse('main:customer-detail', args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_customer(self):
        url = reverse('main:edit-customer', args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_customer(self):
        url = reverse('main:delete-customer', args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)



class OrderAPITest(APITestCase):
    def setUp(self):
        Order.objects.create(
            item = 'iphone', 
            amount = 1000, 
            time = datetime.datetime.now()
        )

    def test_orders_list(self):
        url = reverse('main:order-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_order_create(self):
        url = reverse('main:order-list')
        response = self.client.post(url, {'item': 'iphone', 'amount':1000, 'time':datetime.datetime.now()})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_order_detail(self):
        url = reverse('main:order-detail', args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)





