# Generated by Django 3.1.7 on 2022-07-11 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='participants',
            field=models.IntegerField(default=0),
        ),
    ]
