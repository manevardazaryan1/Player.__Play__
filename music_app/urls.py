from django.urls import path

from music_app import views


app_name = "music_app"

urlpatterns = [
    path('music/', views.MusicView.as_view(), name='music'),
    path('player', views.PlayerView.as_view(), name='player'),
    path('music/detail/<slug:slug>/', views.MusicDetailView.as_view(), name='detail'),
    path('music/add/', views.add_music_to_playlist, name='add_music_to_playlist'),
    path('save-comment/', views.save_comment, name='save_comment'),
    path('playlists/', views.PlaylistView.as_view(), name='playlists'),
    path('playlist/create/', views.create_playlist, name='create_playlist'),
    path('playlist/<str:playlist_name>/', views.playlist_detail, name="playlist_detail"),
    path('playlist/delete/<int:pk>/', views.DeletePlaylistView.as_view(), name="delete_playlist"),
    path('playlist/delete/<str:playlist_name>/<slug:slug>/', views.delete_music_from_playlist, name="delete_music_from_playlist"),
    path('like-song/', views.like_song, name="like_song")
]