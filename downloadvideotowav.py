from pytube import YouTube
from pydub import AudioSegment
import os

url = "https://www.youtube.com/watch?v=xrMvk-qXSuQ"

def descargar_audio_youtube(url,destino_pasta):
    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).first()
    destino = destino_pasta
    out_file = video.download(output_path=destino)
    base, ext = os.path.splitext(out_file)
    print(base)
    audio = AudioSegment.from_file(out_file)
    new_file =  base + '.wav'
    audio.export(new_file, format='wav')

    os.remove(out_file)
    print(new_file)

    return new_file

descargar_audio_youtube(url,destino_pasta='')
