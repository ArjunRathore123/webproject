# Generated by Django 5.0 on 2024-01-09 14:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_order_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='cartitem',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.cartitem'),
        ),
    ]