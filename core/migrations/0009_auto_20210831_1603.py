# Generated by Django 3.2.6 on 2021-08-31 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20210831_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquete',
            name='option_four',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='enquete',
            name='option_one',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='enquete',
            name='option_three',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='enquete',
            name='option_two',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
