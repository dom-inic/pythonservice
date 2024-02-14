from django.test import TestCase
from ..serializers import CustomerSerializer, OrderSerializer
import datetime
# unit test for CustomerSerializer 
class CustomerSerializerTest(TestCase):
    def test_serializer_valid_data(self):
        data = {'name': 'richard', 'code': 'hjdshg3'}
        serializer = CustomerSerializer(data=data)
        self.assertTrue(serializer.is_valid())


# unit test for OrderSerializer
class OrderSerializerTest(TestCase):
    def setUp(self):
        self.data = {'item': 'mouse', 'amount': 5635, 'time': datetime.datetime.now()}
        self.serializer = OrderSerializer(data=self.data)
    def test_serializer_valid_data(self):
        self.assertTrue(self.serializer.is_valid())


