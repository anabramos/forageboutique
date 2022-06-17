# Generated by Django 3.2.13 on 2022-06-17 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0006_orderreview'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderreview',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='orderreview',
            name='image_url',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
    ]
