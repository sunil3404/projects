# Generated by Django 4.1 on 2023-06-20 03:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0004_rename_user_id_orderitem_user_ids"),
    ]

    operations = [
        migrations.RenameField(
            model_name="orderitem",
            old_name="user_ids",
            new_name="user_id",
        ),
    ]