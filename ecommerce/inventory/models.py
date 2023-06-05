from django.db import models
# Create your models here.

class Inventory(models.Model):

    category = models.CharField(max_length=100, unique=True)
    quantity = models.IntegerField(default=0)


    def __str__(self):
        return self.category
