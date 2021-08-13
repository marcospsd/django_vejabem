from django.contrib import admin
from core.models import Post


# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id","title","slug", "author", "created", "update")
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ['created']
