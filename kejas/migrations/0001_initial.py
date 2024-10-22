# Generated by Django 3.0.6 on 2020-07-18 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyKeja',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_name', models.CharField(max_length=200, unique=True)),
                ('property_image', models.ImageField(blank=True, upload_to='keja_pics')),
                ('description', models.TextField(max_length=1000)),
                ('location', models.CharField(max_length=100)),
                ('phone_no', models.IntegerField()),
                ('email_address', models.EmailField(max_length=254)),
                ('more_property_images', models.ImageField(blank=True, upload_to='keja_pics')),
                ('property_specs', models.CharField(max_length=300)),
                ('published_date', models.DateTimeField(auto_now=True)),
                ('category', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'mykejas',
            },
        ),
    ]
