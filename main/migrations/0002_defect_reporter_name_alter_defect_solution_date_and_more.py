# Generated by Django 5.0.1 on 2024-01-11 23:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="defect",
            name="reporter_name",
            field=models.CharField(
                default="",
                help_text="Nom de la personne rapportant l'erreur",
                max_length=255,
                verbose_name="Nom et prénom",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="defect",
            name="solution_date",
            field=models.DateField(
                blank=True, editable=False, null=True, verbose_name="date de résolution"
            ),
        ),
        migrations.AlterField(
            model_name="defect",
            name="status",
            field=models.CharField(
                choices=[
                    ("OPEN", "ouvert"),
                    ("SOLVED", "résolu"),
                    ("CANCELLED", "annulé"),
                ],
                default="OPEN",
                max_length=255,
                verbose_name="statut",
            ),
        ),
        migrations.AlterField(
            model_name="location",
            name="comment",
            field=models.TextField(blank=True, verbose_name="notes"),
        ),
        migrations.AlterField(
            model_name="vehicle",
            name="carburant",
            field=models.CharField(
                choices=[
                    ("DIESEL", "Gasoil"),
                    ("UNLEADED_95_10", "SP 95-E10"),
                    ("UNLEADED_98", "SP 98"),
                    ("ETHANOL", "E85"),
                    ("ELECTRIC", "Électrique"),
                ],
                max_length=255,
                verbose_name="carburant",
            ),
        ),
        migrations.AlterField(
            model_name="vehicle",
            name="status",
            field=models.CharField(
                choices=[
                    ("OPERATIONAL", "Opérationnel"),
                    ("IN_REPAIR", "En réparation"),
                    ("OUT_OF_ORDER", "En panne"),
                ],
                default="OPERATIONAL",
                max_length=255,
                verbose_name="statut",
            ),
        ),
        migrations.AlterField(
            model_name="vehicle",
            name="type",
            field=models.CharField(
                choices=[("VTP", "VTP - Véhicule de Transport de Personnel")],
                max_length=255,
                verbose_name="type de véhicule",
            ),
        ),
    ]
