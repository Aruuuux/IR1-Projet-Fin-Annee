# Generated by Django 4.2.13 on 2024-06-07 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("databaseprojet", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Hours",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("start_time", models.TimeField()),
                ("end_time", models.TimeField()),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="databaseprojet.course",
                    ),
                ),
            ],
        ),
    ]
