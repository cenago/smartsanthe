# Generated by Django 4.1.7 on 2023-03-31 20:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('digital_solar', '0003_customer_address_customer_mobile_voltages'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='voltages',
            options={'verbose_name_plural': 'Voltages'},
        ),
    ]