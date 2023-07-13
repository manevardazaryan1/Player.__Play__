from django.contrib import admin

from .models import Comment, Music, Playlist, Like

# Register your models here.

class MusicAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Music, MusicAdmin)
admin.site.register(Comment)
admin.site.register(Playlist)
admin.site.register(Like)