# Generated by Django 3.2.12 on 2022-04-04 05:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='solicitud',
            options={'ordering': ['created_at'], 'verbose_name_plural': 'Solicitudes'},
        ),
    ]
