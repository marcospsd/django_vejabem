from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    content = RichTextUploadingField()
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
