from moviepy.editor import VideoFileClip
from pathlib import Path


class Video:
    @staticmethod
    def audio(obj):
        video_file = Path(obj) # путь к файлу
        video = VideoFileClip(str(video_file)) # передаем строку пути
        audio = video.audio
        audio.write_audiofile(f"{video_file.stem}.mp3") # сохранить аудио с тем же именем
        video.close() # закрыть видеофайл, освободить ресурсы

Video.audio("airplane.MOV")