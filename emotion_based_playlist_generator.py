import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Spotify API credentials from environment variables
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

# Authenticate with Spotify
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET))

# Function to fetch playlists for a mood
def get_playlists_for_mood(mood):
    try:
        results = sp.search(q=f"{mood} music", type='playlist', limit=5)
        if results and 'playlists' in results and 'items' in results['playlists']:
            playlists = [playlist for playlist in results['playlists']['items'] if playlist is not None]
            return [
                {"name": playlist['name'], "id": playlist['id'], "owner": playlist['owner']['display_name']}
                for playlist in playlists
            ] if playlists else []
        else:
            return []
    except Exception as e:
        st.error(f"Error fetching playlists: {e}")
        return []

# Function to fetch tracks from a playlist
def get_tracks_from_playlist(playlist_id):
    try:
        tracks = sp.playlist_tracks(playlist_id)['items']
        return [
            {
                "name": track['track']['name'],
                "artist": track['track']['artists'][0]['name'],
                "spotify_url": track['track']['external_urls']['spotify']  # Spotify URL for the track
            } for track in tracks
        ]
    except Exception as e:
        st.error(f"Error fetching tracks: {e}")
        return []

# Streamlit App
def main():
    # Custom CSS for styling links
    st.markdown(
        """
        <style>
        .custom-link {
            color: white !important;
            text-decoration: none;
            font-size: 16px;
        }
        .custom-link:hover {
            color: lightgray !important;
            text-decoration: underline;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("Mood-Based Playlist App")

    # Mood input
    mood = st.text_input("Enter your mood:")

    if st.button("Fetch Playlists"):
        if not mood:
            st.error("Please enter a mood.")
        else:
            playlists = get_playlists_for_mood(mood)
            if playlists:
                st.write("Playlists:")
                playlist_names = [f"{playlist['name']} (by {playlist['owner']})" for playlist in playlists]
                selected_playlist = st.selectbox("Select a playlist:", playlist_names)
                if selected_playlist:
                    playlist_id = playlists[playlist_names.index(selected_playlist)]['id']
                    tracks = get_tracks_from_playlist(playlist_id)
                    if tracks:
                        st.write("Tracks:")
                        for track in tracks:
                            # Make the track name clickable and redirect to Spotify
                            track_link = f"<a href='{track['spotify_url']}' target='_blank' class='custom-link'>{track['name']} - {track['artist']}</a>"
                            st.markdown(track_link, unsafe_allow_html=True)
                    else:
                        st.info("No tracks found for this playlist.")
            else:
                st.info("No playlists found for this mood.")

if __name__ == "__main__":
    main()