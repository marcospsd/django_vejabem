# Generated by Django 3.2.6 on 2021-09-17 02:18

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20210902_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youtube',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name='youtube',
            name='summary',
            field=models.CharField(max_length=500),
        ),
    ]