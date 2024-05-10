from pytube import Playlist, YouTube

# Get the playlist URL from the environment variable
playlist_url = "https://www.youtube.com/watch?v=2EYHZ2zUqTg&list=PLgtFJ5i1fDDcpItxvY_UQdvC3bEiNCbSQ"

if not playlist_url:
    print("Error: Playlist URL not found in environment variables.")
    exit(1)

# Create a Playlist object
playlist = Playlist(playlist_url)

# Directory where you want to save the videos
save_path = "/"

# Iterate over all videos in the playlist
for video in playlist.video_urls:
    # Create a YouTube object for the video
    yt = YouTube(video)

    # Get the highest resolution stream
    stream = yt.streams.get_highest_resolution()

    print("Downloading:", yt.title)
    # Download the video to the specified directory
    stream.download(output_path=save_path)
