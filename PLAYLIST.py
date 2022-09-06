import spotipy 
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
import json


spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials())

scope = 'playlist-modify-public'
username = 'shamarphillips'

token = SpotifyOAuth(scope=scope, username=username)
spotifyObject = spotipy.Spotify(auth_manager=token)

def Find_artists(name):
    results = spotify.search(q='artist:'+artist,type='artist')
    id = results['artists']['items'][0]['external_urls']['spotify']
    return id

def get_artist_tracks(num_songs,artist_id):
    result = spotify.artist_top_tracks(Find_artists(artist))
    all_tracks = []
    for track in result['tracks'][:int(num_songs)]:
      all_tracks.append(track['uri'])
    return all_tracks

#create a playlist
playlist_name = input("Enter a playlist name:")
playlist_description = input("Enter a playlist description:")

spotifyObject.user_playlist_create(user=username,name = playlist_name,public=True,description=playlist_description)

num_songs = input("Enter the total songs you want from this each artist:")

artist = input("Enter an artist:")
list_of_songs = []
while artist != "quit":
    songs = get_artist_tracks(num_songs,Find_artists(artist))
    list_of_songs+=songs
    artist = input("Enter another artist or enter quit:")

prePlaylist = spotifyObject.user_playlists(user=username)
playlist = prePlaylist['items'][0]['id']

spotifyObject.user_playlist_add_tracks(user=username,playlist_id=playlist,tracks=list_of_songs)
