# Generated by Django 4.2.1 on 2023-05-30 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmacia', '0003_producto_precioventa_alter_producto_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='descripcion',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='marca',
            name='descripcion',
            field=models.TextField(blank=True, null=True),
        ),
    ]
