# Generated by Django 2.2.13 on 2020-06-18 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitas_granada', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='visita',
            name='foto',
            field=models.FileField(blank=True, upload_to='fotos'),
        ),
    ]
