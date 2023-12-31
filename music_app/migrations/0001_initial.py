# Generated by Django 4.2.2 on 2023-07-13 09:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import music_app.helpers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("singer_app", "0001_initial"),
        ("genre_app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Music",
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
                    "audio",
                    models.FileField(
                        blank=True, upload_to=music_app.helpers.upload_audio
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True, upload_to=music_app.helpers.upload_image
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("is_published", models.BooleanField(default=True)),
                (
                    "slug",
                    models.SlugField(max_length=255, unique=True, verbose_name="URL"),
                ),
                (
                    "artist",
                    models.ManyToManyField(
                        related_name="music", to="singer_app.singer"
                    ),
                ),
                (
                    "genre",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="music_genre",
                        to="genre_app.genre",
                    ),
                ),
                (
                    "users_liked_post",
                    models.ManyToManyField(
                        blank=True,
                        related_name="favorite_songs",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Music",
                "verbose_name_plural": "Music",
            },
        ),
        migrations.CreateModel(
            name="Playlist",
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
                    "music",
                    models.ManyToManyField(
                        blank=True, related_name="playlist_music", to="music_app.music"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="playlist_user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Like",
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
                ("name", models.CharField(default=None, max_length=255)),
                (
                    "liked_songs",
                    models.OneToOneField(
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="music_app.music",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Comment",
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
                ("comment", models.TextField(default="")),
                ("add_time", models.DateTimeField(auto_now_add=True)),
                (
                    "music",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="music_comments",
                        to="music_app.music",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comment_user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
