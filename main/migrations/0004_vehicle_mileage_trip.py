# Generated by Django 5.0.1 on 2024-01-12 18:52

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0003_alter_defect_reporter_name_alter_vehicle_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="vehicle",
            name="mileage",
            field=models.PositiveIntegerField(default=0, verbose_name="kilométrage"),
        ),
        migrations.CreateModel(
            name="Trip",
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
                    "starting_mileage",
                    models.PositiveIntegerField(verbose_name="kilométrage de départ"),
                ),
                (
                    "ending_mileage",
                    models.PositiveIntegerField(
                        blank=True, null=True, verbose_name="kilométrage de fin"
                    ),
                ),
                (
                    "starting_time",
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        verbose_name="heure de départ",
                    ),
                ),
                (
                    "ending_time",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="heure d'arrivée"
                    ),
                ),
                (
                    "driver_name",
                    models.CharField(max_length=255, verbose_name="nom du conducteur"),
                ),
                (
                    "purpose",
                    models.CharField(
                        max_length=255, verbose_name="motif du déplacement"
                    ),
                ),
                (
                    "finished",
                    models.BooleanField(
                        default=False, editable=False, verbose_name="terminé"
                    ),
                ),
                (
                    "vehicle",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main.vehicle",
                        verbose_name="véhicule",
                    ),
                ),
            ],
            options={
                "verbose_name": "trajet",
            },
        ),
    ]