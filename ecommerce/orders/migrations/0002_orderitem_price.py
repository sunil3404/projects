# Generated by Django 4.1 on 2023-07-17 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="orderitem",
            name="price",
            field=models.FloatField(default=0.0),
        ),
    ]
