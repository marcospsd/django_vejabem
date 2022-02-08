from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    summary = models.CharField(max_length=500)
    col1lin1 = RichTextUploadingField(null=True, blank=True)
    col2lin1 = RichTextUploadingField(null=True, blank=True)
    col1lin2 = RichTextUploadingField(null=True, blank=True)
    col2lin2 = RichTextUploadingField(null=True, blank=True)
    col1lin3 = RichTextUploadingField(null=True, blank=True)
    col2lin3 = RichTextUploadingField(null=True, blank=True)
    col1lin4 = RichTextUploadingField(null=True, blank=True)
    col2lin4 = RichTextUploadingField(null=True, blank=True)
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

class Webinar(models.Model):

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
    pageupdate = models.BooleanField(default=False)
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

class Dimaiz(models.Model):
    title = RichTextUploadingField(null=True, blank=True)
    summary = models.CharField(max_length=500)
    content1 = RichTextUploadingField(null=True, blank=True)
    content2 = RichTextUploadingField(null=True, blank=True)
    content3 = RichTextUploadingField(null=True, blank=True)
    content4 = RichTextUploadingField(null=True, blank=True)
    content5 = RichTextUploadingField(null=True, blank=True)
    content6 = RichTextUploadingField(null=True, blank=True)
    content7 = RichTextUploadingField(null=True, blank=True)
    content8 = RichTextUploadingField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class TabelaPreco(models.Model):
    title = models.CharField(max_length=50,null=True, blank=True)
    slug = models.SlugField(max_length=255)
    content = RichTextUploadingField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Circular(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    slug = models.SlugField(max_length=255)
    content1 = RichTextUploadingField(null=True, blank=True)
    content2 = RichTextUploadingField(null=True, blank=True)
    content3 = RichTextUploadingField(null=True, blank=True)
    content4 = RichTextUploadingField(null=True, blank=True)
    content5 = RichTextUploadingField(null=True, blank=True)
    content6 = RichTextUploadingField(null=True, blank=True)
    content7 = RichTextUploadingField(null=True, blank=True)
    content8 = RichTextUploadingField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title