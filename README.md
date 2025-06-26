![Repo Size](https://img.shields.io/github/repo-size/dmitriy347/mov_audio)
![Top Language](https://img.shields.io/github/languages/top/dmitriy347/mov_audio)
![Last Commit](https://img.shields.io/github/last-commit/dmitriy347/mov_audio)

# 🎞️ Audio Extractor from Video (.MOV)

Этот скрипт извлекает аудио из видеофайлов `.MOV` и сохраняет их в формате `.mp3`, используя библиотеку [moviepy](https://zulko.github.io/moviepy/).

## 📦 Зависимости

- Python 3.13 (или 3.10+)
- moviepy

## Пример использования

```python
from aud import Video

a = Video()
a.audio("airplane.MOV")
