# Generated by Django 3.2.13 on 2022-05-22 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderlineitem',
            name='product_size',
        ),
    ]
