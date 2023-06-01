from django.shortcuts import render
from django.http import JsonResponse
from .models import Genre, Artist, Album, Track, Playlist

def index(request):
    # Logic for rendering the index page
    return render(request, 'index.html')

def genre_list(request):
    genres = Genre.objects.all()
    # Serialize genres using GenreSerializer and return as JSON response
    # Example: serialized_data = GenreSerializer(genres, many=True).data
    return JsonResponse(serialized_data)

def artist_list(request):
    artists = Artist.objects.all()
    # Serialize artists using ArtistSerializer and return as JSON response

def album_list(request):
    albums = Album.objects.all()
    # Serialize albums using AlbumSerializer and return as JSON response

def track_list(request):
    tracks = Track.objects.all()
    # Serialize tracks using TrackSerializer and return as JSON response

def playlist_list(request):
    playlists = Playlist.objects.all()
    # Serialize playlists using PlaylistSerializer and return as JSON response

# Add more view functions for other URL patterns as needed
