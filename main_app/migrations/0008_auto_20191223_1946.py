# Generated by Django 2.2.6 on 2019-12-23 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_match_judge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_number',
            field=models.IntegerField(default=1),
        ),
    ]
