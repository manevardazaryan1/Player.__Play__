from django.contrib import admin

from .models import Genre

# Register your models here.

class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Genre, GenreAdmin)
