# Generated by Django 4.1 on 2023-06-20 03:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0003_rename_product_id_cart_product"),
    ]

    operations = [
        migrations.RenameField(
            model_name="orderitem",
            old_name="user_id",
            new_name="user_ids",
        ),
    ]