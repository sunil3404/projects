# Generated by Django 4.1 on 2023-07-18 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="product_offers",
            field=models.IntegerField(default=0),
        ),
    ]