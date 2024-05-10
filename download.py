from pytube import Playlist, YouTube
from pytube.exceptions import VideoUnavailable
import time

# Get the playlist URL from the environment variable
playlist_url = (
    "https://www.youtube.com/playlist?list=PLHxIBAskzRO6X_ClqPjV2mMqTGPQ0OigP"
)

if not playlist_url:
    print("Error: Playlist URL not found in environment variables.")
    exit(1)

# Create a Playlist object
playlist = Playlist(playlist_url)

# Directory where you want to save the videos
save_path = "/data/JT-Videos"


downloaded_count = 0

for index, video_url in enumerate(playlist.video_urls):
    if index < 76:
        continue  # Skip the first 76 videos
    try:
        # Create a YouTube object for the video
        yt = YouTube(video_url)

        # Get the highest resolution stream
        stream = yt.streams.get_highest_resolution()

        print("Downloading:", yt.title)
        # Download the video to the specified directory
        stream.download(output_path=save_path)

        # Increment downloaded count
        downloaded_count += 1

        # Check if downloaded count is a multiple of 10
        if downloaded_count % 10 == 0:
            print("Sleeping for 15 minutes...")
            time.sleep(600)  # Sleep for 10 minutes

    except VideoUnavailable:
        print("Video is unavailable. Skipping...")

    except Exception as e:
        print("An error occurred:", e)

print("Download completed.")
