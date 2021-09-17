from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    summary = models.CharField(max_length=500)
    col1lin1 = RichTextUploadingField(null=True)
    col2lin1 = RichTextUploadingField(null=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Youtube(models.Model):

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    summary = models.CharField(max_length=500, null=False)
    content = RichTextUploadingField(null=False)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Enquete(models.Model):
    active = models.BooleanField(default=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    question = models.TextField()
    option_one = models.CharField(max_length=255, blank=True)
    option_two = models.CharField(max_length=255, blank=True)
    option_three = models.CharField(max_length=255, blank=True)
    option_four = models.CharField(max_length=255, blank=True)
    total_votes = models.IntegerField(default=0)
    option_one_count = models.IntegerField(default=0)
    option_two_count = models.IntegerField(default=0)
    option_three_count = models.IntegerField(default=0)
    option_four_count = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
