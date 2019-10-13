# Generated by Django 2.2.3 on 2019-10-13 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('name', models.CharField(max_length=100, verbose_name='Imię')),
                ('surname', models.CharField(blank=True, max_length=100, verbose_name='Nazwisko')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='E-mail')),
                ('accepted_terms', models.BooleanField(default=False, verbose_name='Akceptuję regulamin serwisu')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
