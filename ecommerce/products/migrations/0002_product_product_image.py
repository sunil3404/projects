# Generated by Django 4.1 on 2023-05-04 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="product_image",
            field=models.ImageField(default="default.jpeg", upload_to="pruduct_images"),
        ),
    ]