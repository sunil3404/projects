# Generated by Django 4.1 on 2023-06-20 03:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="cart",
            old_name="product",
            new_name="product_id",
        ),
    ]