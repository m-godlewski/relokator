# Generated by Django 2.2.3 on 2019-11-10 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20191027_1303'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='name',
        ),
        migrations.RemoveField(
            model_name='account',
            name='surname',
        ),
        migrations.AlterField(
            model_name='account',
            name='first_name',
            field=models.CharField(max_length=100, verbose_name='Imię'),
        ),
        migrations.AlterField(
            model_name='account',
            name='last_name',
            field=models.CharField(blank=True, max_length=100, verbose_name='Nazwisko'),
        ),
    ]
