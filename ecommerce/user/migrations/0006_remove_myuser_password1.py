# Generated by Django 4.1 on 2023-05-17 07:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0005_remove_myuser_password2"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="myuser",
            name="password1",
        ),
    ]
