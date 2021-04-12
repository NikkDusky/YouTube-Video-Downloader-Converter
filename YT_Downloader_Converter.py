from __future__ import unicode_literals
import youtube_dl
import os



# Переменные
info = [] #Словарь, наполняется с помощью youtube_dl в функции get_info(). Берём отсюда id и title, для дальнейшего составления имени файла
video_URL = '' #URL видео всё просто

#Опции для youtube_dl, тихий режим без вывода информации о скачивании.
ydl_opts = {
    'quiet': True #Если хотите видеть прогресс загрузки видео, поставьте здесь False
}



def video_URL_question(): #Форма ввода URL
    global video_URL
    print("\n      YouTube video downloader / converter")
    video_URL = input('\n         Введи URL, желаемого видео: ')
    print("\n")

def download(video): #Функция для загрузки видео
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video])
        os.system("cls")
        print("\n      Видео загружено")

def get_info(video): #Функция для получения информации в глобальную переменную info
    global info
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(video, download=False)
        os.system("cls")
        print("\n\n\n      Видео найдено: " + info['title'])
        print("\n         В процессе загрузки...")
        print("\n")

video_URL_question() #Здесь начинается работа программы, вызываем функцию для ввода URL
get_info(video_URL) #Вызываем функцию для получения информации о названии видео
download(video_URL) #Вызываем функцию для выкачивания видео

def question(): #Функция для выбора последующих действий
    global cont_question #
    print("\n      [/] Опции [/]")
    print("\n         y - Загрузить ещё видео")
    print(f"         d - Перекодировать видео {info['title']} в wav, mp3")
    print("         q - Выйти")
    cont_question = input("\n      Твой выбор: ")
    os.system("cls")
    
def convert_it(file_name): #Функция для кодирования в другой формат, используем библиотеку ffmpeg, которая распологается по пути bin\ffmpeg
    os.system("cls")
    print("\n      Во что перекодировать видео?")
    print("\n         1 - 340 kbps/mp3/Mono")
    print("         2 - 340 kbps/mp3/Stereo")
    print("         3 - WAV / Mono")
    print("         4 - Wav / Stereo")
    audio_quality_choice = input("\n      Твой выбор: ")
    
    #Ифы для выбора варианта кодирования
    if audio_quality_choice == "1":
        os.system(f"bin\\ffmpeg -i {file_name} -vn -ar 44100 -ac 1 -b:a 340k -f mp3 {file_name}.mp3")
    elif audio_quality_choice == "2":
        os.system(f"bin\\ffmpeg -i {file_name} -vn -ar 44100 -b:a 340k -f mp3 {file_name}.mp3")
    elif audio_quality_choice == "3":
        os.system(f"bin\\ffmpeg -i {file_name} -vn -ar 44100 -ac 1 -f wav {file_name}.wav")
    else:
        os.system(f"bin\\ffmpeg -i {file_name} -vn -ar 44100 -f wav {file_name}.wav")

    os.system("cls")
    print(f"\n      Готово!\n      {file_name}\n      Успешно перекодирован и лежит рядом со скриптом!")

while True: #Бесконечный цикл
    
    os.system("cls")
    question() #Вызов функции выбора последующих действий

    #Вызов функций в зависимости от выбора
    if cont_question == "y":
        video_URL_question()
        get_info(video_URL)
        download(video_URL)
    
    if cont_question == "d":
        video_file_name = ('"' + info['title'] + '-' + info['id'] + '.mp4' + '"')
        convert_it(video_file_name)
        
    if cont_question == "q":
        exit()