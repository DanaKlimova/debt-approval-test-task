# Generated by Django 5.1 on 2024-08-26 19:16
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="DebtRequest",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("name", models.CharField(max_length=200)),
            ],
            options={"abstract": False},
        ),
        migrations.CreateModel(
            name="Manufacturer",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("name", models.CharField(max_length=200)),
            ],
            options={"abstract": False},
        ),
        migrations.CreateModel(
            name="Contract",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("name", models.CharField(max_length=200)),
                (
                    "debt_request", 
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.DO_NOTHING, 
                        related_name="contract", 
                        to="debt_approval_api.debtrequest",
                    ),
                ),
            ],
            options={"abstract": False},
        ),
        migrations.CreateModel(
            name="Item",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("name", models.CharField(max_length=200)),
                (
                    "debt_request", 
                     models.ForeignKey(
                         on_delete=django.db.models.deletion.DO_NOTHING,
                         related_name="items",
                         to="debt_approval_api.debtrequest",
                     ),
                 ),
                (
                    "manufacturer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING, 
                        to="debt_approval_api.manufacturer",
                    ),
                ),
            ],
            options={"abstract": False},
        ),
    ]
