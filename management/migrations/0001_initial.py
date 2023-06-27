# Generated by Django 4.2.2 on 2023-06-26 08:01

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("seller", "0004_rename_business_number_business_business"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "categorykey",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("category_number", models.CharField(max_length=20)),
                ("big_group", models.CharField(max_length=20)),
                ("medium_group", models.CharField(max_length=20)),
                ("small_group", models.CharField(blank=True, max_length=20, null=True)),
                (
                    "categoryforeignkey",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="seller.market"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Inventory",
            fields=[
                (
                    "Inventorykey",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("barcode", models.IntegerField()),
                ("Inventory_name", models.CharField(max_length=30)),
                ("Inventory_price", models.IntegerField()),
                ("origin", models.CharField(max_length=30)),
                ("weight", models.CharField(blank=True, max_length=20, null=True)),
                ("count", models.CharField(blank=True, max_length=20, null=True)),
                ("manufacture", models.CharField(max_length=20)),
                ("sale", models.BooleanField()),
                (
                    "inventoryforeignkey",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="management.category",
                    ),
                ),
            ],
        ),
    ]
