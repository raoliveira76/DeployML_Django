# Generated by Django 4.1.1 on 2022-09-16 02:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('endpoints', '0002_mlalgorithmstatus_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mlalgorithmstatus',
            name='owner',
        ),
    ]
