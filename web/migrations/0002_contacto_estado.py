# Generated by Django 5.0.6 on 2024-06-28 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacto',
            name='estado',
            field=models.CharField(choices=[('pendiente', 'Pendiente'), ('en_proceso', 'En Proceso'), ('realizado', 'Realizado')], default='pendiente', max_length=20),
        ),
    ]
