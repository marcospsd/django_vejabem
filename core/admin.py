from django.contrib import admin
from core.models import Post, Youtube, Enquete, Webinar, Dimaiz, Circular, TabelaPreco
from ckeditor.widgets import CKEditorWidget


# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "slug", "author", "created", "update")
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ['created']


@admin.register(Youtube)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "slug", "author", "created", "update")
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ['created']

@admin.register(Enquete)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "slug", "option_one", "option_two", "option_three","option_four")
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ['created']

@admin.register(Webinar)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "slug", "author", "created", "update")
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ['created']

@admin.register(Dimaiz)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author", "created", "update")
    list_filter = ['created']

@admin.register(TabelaPreco)
class TabelaPrecosAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author", "created_at")
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ['created_at']

@admin.register(Circular)
class CircularAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author", "created_at")
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ['created_at']