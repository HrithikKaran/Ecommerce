# Generated by Django 5.0 on 2023-12-27 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_order_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='amount',
            field=models.IntegerField(default='0'),
        ),
    ]
