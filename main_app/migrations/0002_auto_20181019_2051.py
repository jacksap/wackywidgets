# Generated by Django 2.1.2 on 2018-10-19 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='widget',
            name='description',
            field=models.IntegerField(),
        ),
    ]
