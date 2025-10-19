from pytube import YouTube
import os

def download_video(url, output_path='C:/Users/rafae/Desktop/UTFPR/Extensão/IC/Esportes Python'):
    try:
        # Create a YouTube object
        yt = YouTube(url)

        video = yt.streams.get_highest_resolution()

        if output_path == 'C:/Users/rafae/Desktop/UTFPR/Extensão/IC/Esportes Python':
            output_path = os.getcwd()

    
        print(f"Downloading: {yt.title}")
        video.download(output_path)
        print("Download completed!")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage
if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    download_video(video_url)