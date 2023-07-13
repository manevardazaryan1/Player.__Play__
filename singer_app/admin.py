from django.contrib import admin

from .models import Singer

# Register your models here.

class SingerAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Singer, SingerAdmin)