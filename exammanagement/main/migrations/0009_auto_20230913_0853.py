# Generated by Django 3.2.20 on 2023-09-13 01:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_subject_enrollers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='question_id',
            new_name='question',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='chapter_id',
            new_name='chapter',
        ),
    ]