from typing import Any, Dict
from django.shortcuts import render, redirect
from django.views.generic import (TemplateView)
from user_app.models import Profile
from music_app.models import Music
from genre_app.models import Genre
import itertools
# base_app views classes and functions.

class IndexView(TemplateView):
    """Home page template class - IndexView(base)"""
    template_name = "../templates/base_app/index.html"

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        music = Music.objects.all().order_by('-pk')

        context['genres'] = Genre.objects.all()
        if music:
            music = sorted(music, key=lambda x: len(x.users_liked_post.all()))

            context['trending_songs'] = music[::-1][:5]

            recomended_ = [i.artist.all() for i in music]
            merged = list(set(itertools.chain.from_iterable(recomended_)))
            context['recomended_artists'] = merged[:5]

        return context

class AboutView(TemplateView):
    """About page template class - IndexView(base)"""
    template_name = "../templates/base_app/about.html"