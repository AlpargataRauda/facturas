# Generated by Django 3.2.4 on 2021-06-26 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('factura', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lineafactura',
            name='iva',
            field=models.FloatField(default=1.21),
        ),
    ]
