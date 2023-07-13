from django.contrib.auth.models import User
from django.db import models
import uuid
from django.urls import reverse
from .helpers import upload_image


class Genre(models.Model):
    name = models.CharField(max_length=155)
    image = models.ImageField(upload_to=upload_image, blank=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL', default=uuid.uuid1)

    def __str__(self):
        """Genre class str function"""

        return self.name
    
    def get_absolute_url(self):
        """Genre class meta class get absolute url function"""

        return reverse('genre_app:detail', kwargs={'slug': self.slug})
    
    def Genre_list(self):
        """Genres list function"""
        
        return ''.join([i.name for i in self.music_genre.all()])