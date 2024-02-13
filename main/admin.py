from django.contrib import admin
from . models import Customer, Order

class AdminCustomer(admin.ModelAdmin):
    list_display = ('name', 'code')
    search_fields = ('name',)

class AdminOrder(admin.ModelAdmin):
    list_display = ('item', 'amount', 'time')
    search_fields = ('item',)
    list_filter = ('time',)

admin.site.register(Customer, AdminCustomer)
admin.site.register(Order, AdminOrder)
