# Generated by Django 4.2.1 on 2023-05-30 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmacia', '0002_detalleventa_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='precioVenta',
            field=models.DecimalField(decimal_places=3, default=True, max_digits=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.TextField(blank=True, null=True),
        ),
    ]
