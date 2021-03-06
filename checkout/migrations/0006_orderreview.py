# Generated by Django 3.2.13 on 2022-06-17 00:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('products', '0005_alter_product_size'),
        ('checkout', '0005_order_user_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.userprofile')),
                ('order_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='checkout.order')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.product')),
            ],
        ),
    ]
