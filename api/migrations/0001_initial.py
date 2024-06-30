# Generated by Django 5.0.6 on 2024-06-24 23:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ObraArte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('imagen', models.ImageField(upload_to='obras/')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('estilo', models.CharField(choices=[('impresionismo', 'Impresionismo'), ('romanticismo', 'Romanticismo'), ('surrealismo', 'Surrealismo')], max_length=50)),
                ('artista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]