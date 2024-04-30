from pytube import YouTube
import ffmpeg
import os

# Define the path where you want to save videos.
save_path = './output_videos'

# Open the file with YouTube URLs.
with open('links.txt', 'r') as file:
    # Read each line in the file.
    for url in file:
        try:
            # Initialize the YouTube object.
            yt = YouTube(url.strip())

            # Get the title and the upload date.
            title = yt.title
            upload_date = yt.publish_date.strftime('%Y-%m-%d')

            # Filter out characters that are invalid for filenames.
            title_safe = ''.join(char if char.isalnum() else "_" for char in title)

            # Prefix the title with the upload timestamp.
            filename = f"{title_safe}_{upload_date}.mp4"

            # Get the highest resolution video stream.
            video_stream = yt.streams.get_highest_resolution()

            # Download the video.
            print(f"Downloading {title}...")
            video_stream.download(output_path=save_path, filename=filename)
            print(f"Downloaded {title}")

            # Convert the downloaded video to AV1 format.
            print(f"Converting {filename} to AV1...")
            ffmpeg.input(os.path.join(save_path, filename)).output(os.path.join(save_path, f"{title_safe}_{upload_date}.av1"), codec='libaom-av1', crf=30).run(overwrite_output=True)
            print(f"Converted {filename} to AV1")


            # Delete the original MP4 file.
            os.remove(os.path.join(save_path, filename))
        except Exception as e:
            print(f"Failed to download {url.strip()}: {e}")

# Output to let the user know the process is done.
print("All videos have been downloaded.")