# Generated by Django 3.1.7 on 2021-03-06 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mgkeit_app', '0004_auto_20210306_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='build',
            name='mill',
            field=models.CharField(max_length=20, verbose_name='Новый корпус'),
        ),
    ]
