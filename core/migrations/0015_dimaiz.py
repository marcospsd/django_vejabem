# Generated by Django 3.2.6 on 2022-01-18 18:39

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0014_webinar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dimaiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255)),
                ('summary', models.CharField(max_length=500)),
                ('content1', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('content2', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('content3', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('content4', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('content5', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('content6', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('content7', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('content8', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]