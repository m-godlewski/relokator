# Generated by Django 2.2.3 on 2019-11-10 10:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adverts', '0004_auto_20191022_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advert',
            name='user',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
