from django.db import models
from products.models import Product
from django.contrib.auth.models import User
from user.models import MyUser

# Create your models here.

#class Order(models.Model):
#    user_id= models.ForeignKey(MyUser, default="null", on_delete=models.CASCADE)

class OrderItem(models.Model):
    PREORDER = "PREORDER"
    PENDING  = "PENDING"
    ORDERED  = "ORDERED"
    DELIVERED = "DELIVERED"
    CANCELLED = "CANCELLED"

    ORDER_STATUS_CHOICES = [
    ("PREORDER", "PREORDER"),
    ("PENDING", "PENDING"),
    ("ORDERED", "ORDERED"),
    ("DELIVERED", "DELIVERED"),
    ("CANCELLED", "CANCELLED"),
    ]
    user_id = models.ForeignKey(MyUser, default="null", on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, default="null", on_delete=models.CASCADE)
    order_status = models.CharField(max_length=100, choices=ORDER_STATUS_CHOICES, default=PREORDER)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.order_status

class Transaction(models.Model):
    order_id = models.ForeignKey(OrderItem, default="null", on_delete=models.CASCADE)
    #product_id = models.ForeignKey(Product, default="null", on_delete=models.CASCADE)

class Cart(models.Model):
    product = models.ForeignKey(Product, default="null", on_delete=models.CASCADE)

