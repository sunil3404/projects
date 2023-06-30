from django.contrib import admin
from orders.models import Transaction, OrderItem, Cart

# Register your models here.

admin.site.register(Transaction)
#admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Cart)
