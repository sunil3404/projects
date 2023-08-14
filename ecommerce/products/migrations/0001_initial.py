# Generated by Django 4.1 on 2023-06-30 02:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("inventory", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Brand",
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
                ("brand_name", models.CharField(max_length=100, unique=True)),
                ("brand_quantity", models.IntegerField(default=0)),
                (
                    "inventory_id",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="inventory.inventory",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Product",
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
                ("product_name", models.CharField(max_length=100, unique=True)),
                ("product_description", models.TextField()),
                (
                    "product_image",
                    models.ImageField(
                        default="default.jpeg", upload_to="product_images"
                    ),
                ),
                (
                    "product_price",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=5, null=True
                    ),
                ),
                ("product_added_date", models.DateField(auto_now_add=True)),
                ("product_updated_date", models.DateField(auto_now=True)),
                (
                    "brand_id",
                    models.ForeignKey(
                        default="null",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.brand",
                    ),
                ),
                (
                    "category_id",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="inventory.inventory",
                    ),
                ),
            ],
        ),
    ]
