# Generated by Django 4.2.2 on 2023-07-11 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("user_app", "0002_remove_profile_date_of_birth_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="image",
        ),
    ]
