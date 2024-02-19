from celery import shared_task
from . models import Order
import os 
import requests 

@shared_task
def order_created(order_id):
    """ Task to send sms through africa's talking when order has been created successfully"""
    order = Order.objects.get(id=order_id)
    payload = {
        "username": 'sandbox',
        "to": f"{+254791331443}",
        "message": f'your order for {order.item} has been created successfully',
        "from": 53624  
    }

    header = {
        "Accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded",
        'apiKey': os.environ['API_KEY']

    }
    req = requests.post('https://api.sandbox.africastalking.com/version1/messaging', data=payload, headers=header)
    req = req.json()
    message_data = req['SMSMessageData']
    status = message_data["Recipients"][0]['status']
    return status
