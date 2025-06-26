from moviepy.editor import VideoFileClip
from pathlib import Path


class Video:
    @staticmethod
    def extract_audio(filepath: str) -> str:
        """Извлекает аудиодорожку из видеофайла и сохраняет её как .mp3.

        Args:
            filepath (str): Путь к видеофайлу (.MOV)

        Returns:
            str: Путь к сохранённому mp3-файлу
        """
        video_file = Path(filepath)
        if not video_file.exists():
            raise FileNotFoundError(f"Файл не найден: {video_file}")

        output_path = video_file.with_suffix('.mp3')

        with VideoFileClip(str(video_file)) as video:
            video.audio.write_audiofile(str(output_path))

        return str(output_path)


if __name__ == "__main__":
    Video.extract_audio("airplane.MOV")
