# Generated by Django 5.1.2 on 2024-10-18 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_bibliotheque', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auteur',
            name='deadday',
        ),
    ]
