# Generated by Django 4.0.4 on 2022-05-31 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viajes', '0003_alter_viaje_fecha_salida'),
    ]

    operations = [
        migrations.AddField(
            model_name='destino',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
