# Generated by Django 3.2.20 on 2023-09-29 01:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0018_auto_20230927_1736"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="introduction",
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
