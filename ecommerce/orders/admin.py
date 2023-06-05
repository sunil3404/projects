from django.contrib import admin
from orders.models import Transaction, Order, OrderItem

# Register your models here.

admin.site.register(Transaction)
admin.site.register(Order)
admin.site.register(OrderItem)
