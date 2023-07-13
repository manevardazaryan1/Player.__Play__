from django.urls import path

from genre_app import views


app_name = "genre_app"

urlpatterns = [
    path('genre/', views.GenreView.as_view(), name='genre'),
    path('genre/detail/<slug:slug>/', views.GenreDetailView.as_view(), name='detail'),
]