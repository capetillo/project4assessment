# Generated by Django 2.2.6 on 2019-12-28 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_photo_team'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='team',
        ),
    ]