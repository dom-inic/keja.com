# Generated by Django 3.0.6 on 2020-07-21 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kejas', '0003_auto_20200720_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mykeja',
            name='more_property_images',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='mykeja',
            name='property_image',
            field=models.ImageField(upload_to=''),
        ),
    ]
