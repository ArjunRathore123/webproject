# Generated by Django 5.0 on 2024-01-12 05:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_sellerwallet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='country',
        ),
        migrations.RemoveField(
            model_name='order',
            name='state',
        ),
    ]