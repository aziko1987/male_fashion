# Generated by Django 4.1.2 on 2022-10-17 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BannerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collection', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('banner_image', models.ImageField(upload_to='banners/')),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'banner',
                'verbose_name_plural': 'banners',
            },
        ),
    ]
