from pytube import YouTube

url = input('Укажите ссылку на видео:\n')

youtube = YouTube(url)

video = youtube.streams.filter(progressive=True).desc().first()

video.download()
print(f"'{youtube.title}' успешно загружен!\nПродолжительность: "
      f"{(youtube.length)//3600}:{(youtube.length)//60}:{(youtube.length)%60}")