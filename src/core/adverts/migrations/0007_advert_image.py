# Generated by Django 2.2.3 on 2019-08-17 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adverts', '0006_auto_20190816_1513'),
    ]

    operations = [
        migrations.AddField(
            model_name='advert',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
    ]
