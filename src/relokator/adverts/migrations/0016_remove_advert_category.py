# Generated by Django 2.2.3 on 2019-09-19 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adverts', '0015_auto_20190919_1622'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advert',
            name='category',
        ),
    ]
