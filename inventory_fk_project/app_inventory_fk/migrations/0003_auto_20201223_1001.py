# Generated by Django 3.1.4 on 2020-12-23 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_inventory_fk', '0002_item_serial_number'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Marque',
            new_name='Brand',
        ),
    ]
