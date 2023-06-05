# Generated by Django 4.1 on 2023-05-09 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0008_brand_inventory_id"),
        ("orders", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="product_id",
        ),
        migrations.RemoveField(
            model_name="order",
            name="quantity",
        ),
        migrations.CreateModel(
            name="OrderItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "order_status",
                    models.CharField(
                        choices=[
                            ("PREORDER", "PREORDER"),
                            ("PENDING", "PENDING"),
                            ("ORDERED", "ORDERED"),
                            ("DELIVERED", "DELIVERED"),
                            ("CANCELLED", "CANCELLED"),
                        ],
                        default="PREORDER",
                        max_length=100,
                    ),
                ),
                ("quantity", models.IntegerField()),
                (
                    "order_id",
                    models.ForeignKey(
                        default="null",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="orders.order",
                    ),
                ),
                (
                    "product_id",
                    models.ForeignKey(
                        default="null",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.product",
                    ),
                ),
            ],
        ),
    ]
