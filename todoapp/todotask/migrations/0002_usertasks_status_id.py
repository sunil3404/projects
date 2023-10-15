# Generated by Django 4.1 on 2023-10-10 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("status", "0001_initial"),
        ("todotask", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="usertasks",
            name="status_id",
            field=models.ForeignKey(
                default=1,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="status.taskstatus",
            ),
        ),
    ]