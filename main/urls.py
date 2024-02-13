from django.urls import path
from . import views 

urlpatterns = [
    path('', views.CustomerList.as_view(), name='customer-list'),
    path('customerdetail/<pk>/', views.CustomerDetail.as_view(), name='customer-detail'),
    path('editcustomer/<pk>/', views.EditCustomer.as_view(), name='edit-customer'),
    path('deletecustomer/<pk>/', views.DeleteCustomer.as_view(), name='delete-customer'),

    path('orders/', views.OrderList.as_view(), name='order-list'),
    path('order/<pk>/', views.OrderDetail.as_view(), name='order-detail'),
]
