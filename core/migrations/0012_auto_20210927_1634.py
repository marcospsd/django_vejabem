# Generated by Django 3.2.6 on 2021-09-27 19:34

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20210916_2318'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='col1lin2',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='col1lin3',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='col1lin4',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='col2lin2',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='col2lin3',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='col2lin4',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
    ]
