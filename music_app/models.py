from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError
import uuid
from user_app.models import User
from singer_app.models import Singer
from genre_app.models import Genre

from .helpers import upload_image, upload_audio, upload_video

# music_app models.py

class Music(models.Model):
    """Music model class"""

    name = models.CharField(max_length=155)
    genre = models.ForeignKey(Genre, related_name='music_genre', on_delete=models.CASCADE)
    artist = models.ManyToManyField(Singer, related_name='music')
    audio = models.FileField(upload_to=upload_audio, blank=True)
    image = models.ImageField(upload_to=upload_image, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL', default=uuid.uuid1)
    users_liked_post = models.ManyToManyField(User, blank=True, related_name='favorite_songs')

    class Meta:
        """Music class meta class"""

        verbose_name = "Music"
        verbose_name_plural = "Music"

    def __str__(self):
        """Music class str function"""

        return self.name


    def get_absolute_url(self):
        """Music class meta class get absolute url function"""

        return reverse('music_app:detail', kwargs={'slug': self.slug})


class Comment(models.Model):
    """Comments model"""
    
    music = models.ForeignKey(Music, related_name='music_comments', on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comment_user')
    comment = models.TextField(default='')
    add_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment
    

# Playlist

class Playlist(models.Model):

    """Playlist for autenticated users"""
    user = models.ForeignKey(User, related_name='playlist_user', on_delete=models.CASCADE)
    name = models.CharField(max_length=155, )
    music = models.ManyToManyField(Music, related_name='playlist_music', blank=True)

    def clean(self, *args, **kwargs):
        """Save method for playlist"""
        playlist = Playlist.objects.filter(name=self.name, user=self.user).first()

        if playlist and not playlist.pk:
            raise ValidationError("Playlist with this name allredy exists")
        
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        """Music class meta class get absolute url function"""

        return reverse('music_app:playlist_detail', kwargs={'playlist_name': self.name})

class Like(models.Model):
    name = models.CharField(max_length=255, default=None)
    liked_songs = models.OneToOneField(Music, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.name