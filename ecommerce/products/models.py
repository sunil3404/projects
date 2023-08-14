from django.db import models
from inventory.models import Inventory

# Create your models here.
class Brand(models.Model):
    brand_name = models.CharField(max_length=100, unique=True)
    brand_quantity = models.IntegerField(default=0)

    inventory_id = models.ForeignKey(Inventory, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return self.brand_name


class Product(models.Model):
    product_name = models.CharField(max_length=100, unique=True)
    product_description = models.TextField()
    product_image = models.ImageField(default="default.jpeg", upload_to="product_images")
    product_price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    product_added_date = models.DateField(auto_now_add=True)
    product_updated_date = models.DateField(auto_now=True)
    product_offers = models.IntegerField(default=0)

    brand_id = models.ForeignKey(Brand, default="null", on_delete=models.CASCADE)
    category_id  =  models.ForeignKey(Inventory, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name
