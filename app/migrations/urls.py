from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('genres/', views.genre_list, name='genre_list'),
    path('artists/', views.artist_list, name='artist_list'),
    path('albums/', views.album_list, name='album_list'),
    path('tracks/', views.track_list, name='track_list'),
    path('playlists/', views.playlist_list, name='playlist_list'),
    # Add more URL patterns as needed
]
