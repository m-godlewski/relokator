# Generated by Django 2.2.3 on 2019-09-19 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adverts', '0011_advert_prize'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advert',
            name='prize',
            field=models.CharField(max_length=10),
        ),
    ]
