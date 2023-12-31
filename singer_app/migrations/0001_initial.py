# Generated by Django 4.2.2 on 2023-07-13 09:44

from django.db import migrations, models
import singer_app.helpers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("genre_app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Singer",
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
                ("name", models.CharField(max_length=155)),
                (
                    "image",
                    models.ImageField(
                        blank=True, upload_to=singer_app.helpers.upload_image
                    ),
                ),
                (
                    "slug",
                    models.SlugField(max_length=255, unique=True, verbose_name="URL"),
                ),
                (
                    "genre",
                    models.ManyToManyField(
                        related_name="singer_genre", to="genre_app.genre"
                    ),
                ),
            ],
        ),
    ]
