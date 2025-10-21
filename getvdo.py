from pytubefix import YouTube
from pytubefix.cli import on_progress  
import os

def download_video(url, output_path='C:/Users/rafae/Desktop/UTFPR/Extensão/IC/Esportes Python'):
    try:
        yt = YouTube(url, on_progress_callback=on_progress)

        video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

        if output_path == 'C:/Users/rafae/Desktop/UTFPR/Extensão/IC/Esportes Python/Proposta-de-IC/Material Bruto':
            output_path = os.getcwd()

    
        print(f"Baixando: {yt.title}")
        video.download(output_path)
        print("Download concluído!")

    except Exception as e:
        print(f"Ocorreu um erro: {str(e)}")

# Exemplo de uso
if __name__ == "__main__":
    video_url = input("Digite a URL do vídeo do YouTube: ")
    download_video(video_url)