# Generated by Django 3.1.3 on 2021-03-28 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Education",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("school", models.CharField(max_length=100)),
                ("lacation", models.CharField(max_length=50)),
                ("duration", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Experience",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("company", models.CharField(max_length=100)),
                ("lacation", models.CharField(max_length=50)),
                ("duration", models.CharField(max_length=50)),
                ("summary", models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name="Interest",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Project",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("duration", models.CharField(max_length=50)),
                ("summary", models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name="Skill",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Technology",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                (
                    "skill",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="portfolio.skill",
                    ),
                ),
            ],
        ),
    ]
