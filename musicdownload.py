import subprocess
import os
from pydub import AudioSegment
from yt_dlp import YoutubeDL



def descargar_audio_youtube(url, destino_pasta=''):
    # Obter informações do vídeo ou playlist, incluindo o título
    with YoutubeDL({'quiet': True}) as ydl:
        info = ydl.extract_info(url, download=False)
        
        # Verificar se é uma playlist ou um vídeo único
        if 'entries' in info:
            # É uma playlist, extraír entradas
            videos = info['entries']
        else:
            # É um vídeo único
            videos = [info]

    for video_info in videos:
        titulo = video_info.get('title', 'audio')

        # Definir o nome do arquivo temporário (MP3) e final (WAV)
        temp_file = os.path.join(destino_pasta, f"{titulo}.mp3")
        new_file = os.path.join(destino_pasta, f"{titulo}.wav")

        # Baixar o áudio do YouTube usando yt-dlp
        subprocess.run(['yt-dlp', '-x', '--audio-format', 'mp3', '-o', temp_file, video_info['webpage_url']], check=True)

        # Verificar se o arquivo foi baixado corretamente
        if not os.path.exists(temp_file):
            raise FileNotFoundError(f"O arquivo de áudio para '{titulo}' não foi baixado corretamente.")

        # Converter o áudio para formato WAV
        audio = AudioSegment.from_file(temp_file)
        audio.export(new_file, format='wav')

        # Remover o arquivo temporário em MP3
        os.remove(temp_file)

        print(f"Áudio exportado para: {new_file}")

    return True

url = "https://www.youtube.com/watch?v=fLNngcI9NFo"
descargar_audio_youtube(url, destino_pasta='garimpo_maio')


