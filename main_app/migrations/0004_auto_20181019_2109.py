# Generated by Django 2.1.2 on 2018-10-19 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20181019_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='widget',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]