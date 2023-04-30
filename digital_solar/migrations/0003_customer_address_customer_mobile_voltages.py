# Generated by Django 4.1.7 on 2023-03-31 20:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('digital_solar', '0002_alter_customer_service_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='customer',
            name='mobile',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.CreateModel(
            name='Voltages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('volt', models.IntegerField()),
                ('time_instance', models.DateTimeField()),
                ('bill_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Customer', to='digital_solar.customer')),
            ],
            options={
                'verbose_name_plural': 'Customer',
            },
        ),
    ]
