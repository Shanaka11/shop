# Generated by Django 4.0.3 on 2022-07-08 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OrderLines',
            new_name='OrderLine',
        ),
        migrations.AlterModelTable(
            name='orderline',
            table='order_line',
        ),
    ]