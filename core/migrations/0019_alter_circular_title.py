# Generated by Django 3.2.6 on 2022-02-08 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_auto_20220208_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='circular',
            name='title',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
