# Generated by Django 2.2.3 on 2019-09-19 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adverts', '0010_auto_20190918_1546'),
    ]

    operations = [
        migrations.AddField(
            model_name='advert',
            name='prize',
            field=models.CharField(default='1500', max_length=10),
        ),
    ]
