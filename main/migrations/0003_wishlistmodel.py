# Generated by Django 4.1.2 on 2022-11-10 19:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_productmodel_real_price'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0002_contactmessagemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='WishListModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.productmodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'wishlist',
                'verbose_name_plural': 'wishlists',
                'unique_together': {('user', 'product')},
            },
        ),
    ]
