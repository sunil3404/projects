# Generated by Django 4.1 on 2023-05-06 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0005_alter_product_product_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="product_image",
            field=models.ImageField(default="default.jpeg", upload_to="product_images"),
        ),
    ]
