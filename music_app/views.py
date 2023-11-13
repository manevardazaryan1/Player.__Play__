from typing import Any, Dict
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import re
from django.shortcuts import render
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.views.generic import (DetailView, ListView, DeleteView)
from .models import Music, Comment, Playlist, Like
# music_app views classes and functions.

class LoginRequiredMixin:
    """Login required mixin class"""

    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        """Login required dispatch mixin"""

        return super().dispatch(request, *args, **kwargs)

class MusicView(ListView):
    """All songs page template class - MusicView"""

    model = Music
    template_name = '../templates/music_app/all_songs.html'
    context_object_name = 'music'

class PlayerView(ListView):
    model = Music
    template_name = '../templates/music_app/player.html'
    context_object_name = 'music'

class MusicDetailView(DetailView):
    """Music detail page view"""

    queryset = Music.objects.all()
    template_name = '../templates/music_app/song_detail_page.html'
    context_object_name = 'music'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        obj = kwargs['object']
        pk = obj.pk
        data_key = 0
        context['comments_count'] = len(Comment.objects.filter(music=obj))
        context['likes_count'] = len(Music.objects.get(pk=pk).users_liked_post.all())
        music_dict = Music.objects.all().exclude(pk=pk)
        if music_dict:
            data = dict([(Music.objects.get(pk=item.pk), 0) for item in music_dict])
            for key,value in data.items():
                data[key] += len(set(obj.artist.all()).intersection(set(key.artist.all())))
                data[key] += int(obj.genre.name == key.genre.name)
                match = re.search(key.name.upper(),obj.name.upper())

                try:
                    data_key = len(match)
                except:
                    data_key = 0

                data[key] += data_key

            data = sorted(data.items(), key=lambda x:-x[1])[:5]

            related_songs = [i[0] for i in data]

            context['related_songs'] = related_songs


        if not "recently_viewed" in self.request.session:
            self.request.session["recently_viewed"] = []
            self.request.session["recently_viewed"].append(pk)
        else:
            if pk in self.request.session["recently_viewed"]:
                self.request.session["recently_viewed"].remove(pk)
            self.request.session["recently_viewed"].insert(0, pk)
            if len(self.request.session["recently_viewed"]) > 5:
                self.request.session["recently_viewed"].pop()
        self.request.session.modified =True

        recently_viewed = Music.objects.filter(pk__in=self.request.session["recently_viewed"])
        context['recently_viewed'] = sorted(recently_viewed, key=lambda x: self.request.session["recently_viewed"].index(x.pk))
        
        if self.request.user.is_authenticated:
            music = Music.objects.get(pk=pk)
            if any([ i == self.request.user for i in music.users_liked_post.all()]):
                context['like'] = 'unlike'
            else:
                context['like'] = 'like'
            context['playlists'] = Playlist.objects.filter(user=self.request.user)

        return context

class DeletePlaylistView(DeleteView):
	model =  Playlist
	success_url = '/playlists'
	template_name = '../templates/music_app/delete_playlist.html'
	queryset = Playlist.objects.all()

class PlaylistView(LoginRequiredMixin, ListView):
    """All songs page template class - MusicView"""

    template_name = '../templates/music_app/playlists.html'
    paginate_by = 16
    queryset = Playlist.objects.all()
    context_object_name = 'playlists'

    def get_queryset(self):
        self.queryset = self.queryset.filter(user=self.request.user)

        return self.queryset

def save_comment(request):
    """Saved comment"""
    if request.method == 'POST':
        comment = request.POST['comment']
        musicid = request.POST['musicid']
        music = Music.objects.get(pk=musicid)
        user = request.user
        Comment.objects.create(
            music=music,
            comment=comment,
            user=user
        )
        return JsonResponse({'bool': True})
    
def create_playlist(request):
    """Create playlist"""

    if request.method == 'POST':
        playlist_name = request.POST['playlist_name']
        user = request.user
        Playlist.objects.create(
            name=playlist_name,
            user=user
        )
        return JsonResponse({'bool': True})

def playlist_detail(request, playlist_name):

    playlist = get_object_or_404(Playlist, user=request.user, name=playlist_name)
    return render(request, '../templates/music_app/playlist_detail.html', {'playlist': playlist})

def delete_music_from_playlist(request, playlist_name, slug):
    playlist = Playlist.objects.get(user=request.user, name=playlist_name)
    music_ = playlist.music.get(slug=slug)
    playlist.music.remove(music_)
    domain = get_current_site(request)
    return redirect(f'http://{domain}/playlist/{playlist_name}')
    
def add_music_to_playlist(request):
    if request.method == 'POST':
        playlist_name = request.POST['playlist_name']
        music_pk = request.POST['music_pk']
        playlist = Playlist.objects.get(user=request.user, name=playlist_name)
        playlist.music.add(music_pk)

        return JsonResponse({'bool': True})
    
def like_song(request):
    if request.method == 'POST':
        pk = request.POST['music_pk']
        music = Music.objects.get(pk=pk)
        liked = Like.objects.filter(liked_songs=music).first()
        if any([ i == request.user for i in music.users_liked_post.all()]):
            music.users_liked_post.remove(request.user)
        else:
            music.users_liked_post.add(request.user)

        if  not liked:
            Like.objects.create(name=music.name,liked_songs=music)

        return JsonResponse({'bool': True})