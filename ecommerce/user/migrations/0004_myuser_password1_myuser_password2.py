# Generated by Django 4.1 on 2023-05-17 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0003_myuser_address"),
    ]

    operations = [
        migrations.AddField(
            model_name="myuser",
            name="password1",
            field=models.CharField(default="password", max_length=100),
        ),
        migrations.AddField(
            model_name="myuser",
            name="password2",
            field=models.CharField(default="password", max_length=100),
        ),
    ]
