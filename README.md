# Emotion Based Playlist Generator

## Overview
This documentation provides a comprehensive guide to the Emotion-based-playlist-generator implemented using the streamlit library in python. This project allows the user to select a playlist of songs based on his mood and displays the tracks present in the playlist and once the user select his desired track he will be directed to spotify page to listen to the songs.

## TABLE OF CONTENTS

* Features <br>
* Code structure and Function Description<br>
* Visual flow of the app <br>
* How it works<br>
* Conclusion<br>

## FEATURES

* Users can enter their mood to get the playlists based on their mood
* Then five playlists will be displayed and user can select any of the playlist he want
* After selecting the playlist,tracks available in that playlist will be displayed and the user can select any of the track he want
* After selecting the track he will be directed to spotify and then he can listen to any song he want


* Spotify Integration:<br>
        Uses the Spotipy library to interact with the Spotify Web API.Retrieves playlists and tracks based on the user's input mood.
* Dynamic Playlist Search:<br>
        Allows users to input their current mood and fetches playlists relevant to that mood from Spotify.
* Track Details Display:<br>
        Displays track details (name and artist) from a selected playlist.Includes clickable links that open the track on Spotify.
* Web Interface:<br>
        Uses Streamlit to provide a simple and user-friendly web interface for mood input and playlist display.
* Error Handling:<br>
        Gracefully handles errors when fetching playlists or tracks.
* Environment Variable Management:<br>
        Secures API credentials using a .env file and the dotenv library.
* Custom Styling:<br>
        Enhances the user experience with CSS for styling clickable links.

## CODE STRUCTURE AND FUNCTION DESCRIPTIONS

* Imports and Setup:<br>
  * Libraries:<br>
    streamlit: For the web interface.<br>
    spotipy: To interact with Spotify's Web API.<br>
    dotenv: To load environment variables securely.<br>
    os: For environment variable management.<br>
  * Environment Variable Loading:<br>
    Use load_dotenv() to load Spotify credentials (CLIENT_ID, CLIENT_SECRET) from a .env file.
  * Spotify API Authentication:<br>
    Use SpotifyClientCredentials for authentication.
* Helper Functions:<br>
  * get_playlists_for_mood(mood) <br>
    Purpose: Searches Spotify for playlists matching the given mood.<br>
    Key Logic: Calls Spotify's search() API to find playlists.<br>
    Error Handling: Displays error messages if an exception occurs.<br>
  * get_tracks_from_playlist(playlist_id) <br>
    Purpose: Fetches all tracks from the given Spotify playlist.<br>
    Key Logic:Calls Spotify's playlist_tracks() API to retrieve track details.Extracts the track name, artist, and Spotify URL.<br>
    Error Handling: Displays error messages if an exception occurs.<br>
* Main App Logic:<br>
  Function Name: main() <br>
  * Purpose: Handles the Streamlit app interface and workflow.<br>
  * Key Components:<br>
     Custom CSS Styling:Adds styling for clickable links using st.markdown.<br>
     Title Display:Displays the app title using st.title.<br>
     Mood Input:Provides a text input field for the user to enter their mood.<br>
     Fetch Playlists Button:Displays a button that triggers playlist fetching logic.Calls get_playlists_for_mood() and displays the playlists.<br>
     Playlist Selection:Dropdown menu for selecting a playlist from the fetched results.<br>
     Track Fetching and Display:Fetches tracks from the selected playlist using get_tracks_from_playlist().Displays tracks with clickable links to Spotify.<br>
* Entry Point:<br>
   * Condition: if __name__ == "__main__":<br>
   * Purpose: Runs the main() function to start the app.<br>

## VISUAL FLOW OF THE APP

* User Input: Enter mood → Click "Fetch Playlists".<br>
* Playlist Fetching: Calls get_playlists_for_mood(mood) → Displays playlists.<br>
* Playlist Selection: User selects a playlist from the dropdown.<br>
* Track Fetching: Calls get_tracks_from_playlist(playlist_id) → Displays tracks with Spotify links.<br>

## HOW IT WORKS

* Environment Setup:<br>
        Loads Spotify API credentials from a .env file using load_dotenv.
* Authentication:<br>
        Authenticates with Spotify using SpotifyClientCredentials.
* User Interaction:<br>
        Users input their mood in the text box and click the "Fetch Playlists" button.
* Playlist Fetching:<br>
        The app calls get_playlists_for_mood(mood) to retrieve playlists from Spotify based on the mood.
* Playlist Selection:<br>
        Displays the playlist names in a dropdown. Users select one.
* Track Fetching:<br>
        The app calls get_tracks_from_playlist(playlist_id) to retrieve tracks from the selected playlist.
* Track Display:<br>
        Displays track names and artists as clickable links to Spotify.

## CONCLUSION
This app makes the user to get playlists based on his mood accurately and asks his choice to select his wanted tracks.
