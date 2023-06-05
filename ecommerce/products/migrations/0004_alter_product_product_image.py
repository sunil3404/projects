# Generated by Django 4.1 on 2023-05-06 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0003_alter_product_product_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="product_image",
            field=models.ImageField(
                blank=True,
                default="default.jpeg",
                null=True,
                upload_to="pruduct_images",
            ),
        ),
    ]