from django.db import models
from django.urls import reverse
from .helpers import upload_image
from genre_app.models import Genre
import uuid

# singer_app models.py


class Singer(models.Model):
    """Singer model class"""

    name = models.CharField(max_length=155)
    image = models.ImageField(upload_to=upload_image, blank=True)
    genre = models.ManyToManyField(Genre, related_name='singer_genre')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL', default=uuid.uuid1)


    def get_absolute_url(self):
        """Singer class meta class get absolute url function"""

        return reverse('singer_app:detail', kwargs={'slug': self.slug})

    def __str__(self):
        """Singer class str function"""

        return f'{self.name}'
    
    def Singer_list(self):
        """Singer class singer function"""
        
        return ''.join([i.name for i in self.music.all()])
