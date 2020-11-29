# Generated by Django 3.1.3 on 2020-11-24 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Almacen', '0002_auto_20201120_1058'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='eq_vid',
            options={'verbose_name': 'Equipo de video', 'verbose_name_plural': 'Equipo de video'},
        ),
        migrations.AddField(
            model_name='computadora',
            name='Ano',
            field=models.IntegerField(null=True, verbose_name='Año'),
        ),
        migrations.AddField(
            model_name='computadora',
            name='Procesador',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='computadora',
            name='qr_code',
            field=models.ImageField(blank=True, null=True, upload_to='qr_codes'),
        ),
    ]
