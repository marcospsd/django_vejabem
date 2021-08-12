from django.contrib import admin
from core.models import Post


# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "created", "update")
    prepopulated_fields = {"slug": ("title",)}
