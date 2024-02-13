from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=50)

class Order(models.Model):
    # one to many - one customer can have many orders 
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE)
    item = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places= 2)
    time = models.DateTimeField()