# Generated by Django 4.1.7 on 2023-05-01 03:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('product_description', models.TextField()),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('product_added_date', models.DateField(auto_now_add=True)),
                ('product_updated_date', models.DateField(auto_now=True)),
                ('brand_id', models.ForeignKey(default='null', on_delete=django.db.models.deletion.CASCADE, to='products.brand')),
            ],
        ),
    ]