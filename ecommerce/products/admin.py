from django.contrib import admin

from products.models import Product, Brand

# Register your models here.

admin.site.register(Product)
admin.site.register(Brand)
