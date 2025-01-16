import webbrowser
import os
import tkinter as tk
from tkinter import filedialog
from urllib.parse import quote

# Функция для выбора пути к chrome.exe
def path_in_chrome():
    return filedialog.askopenfilename(title="Выберите chrome.exe", filetypes=[("Executable", "*.exe")])

# Функция для выбора папки с профилем
def profile_path():
    return filedialog.askdirectory(title="Выберите папку с профилем")

# Создаём скрытое окно для диалогов
root = tk.Tk()
root.withdraw()

# Функция для создания строки с параметрами запуска браузера
def inc():
    # Путь к браузеру
    chrome_path = path_in_chrome()

    # Режим инкогнито
    incognito_choice = input('Будете ли работать в режиме инкогнито (y/n)? ').strip().lower()
    incognito = True if incognito_choice == 'y' else False

    # Выбор профиля
    profile_choice = input('Будете ли выбирать профиль (y/n)? ').strip().lower()
    profile = None
    if profile_choice == 'y':
        profile = profile_path()

    # Формируем строку запуска
    profile_path_str = f'--profile-directory="{profile}"' if profile else ''
    incognito_flag = ' --incognito' if incognito else ''
    
    return f'"{chrome_path}" {profile_path_str} {incognito_flag}'

# Функции для поиска
def google_define():
    find = input("Что ищем?: ")
    url = f'https://www.google.com/search?q=define {find}'
    # Используем inc() для получения команды с параметрами
    webbrowser.get(inc()).open_new_tab(url)

def google_esv():
    find = input("?: ")
    encoded_find = quote(find)
    url = f'https://www.google.com/search?sca_esv=b49ee4eb3250b196&q={encoded_find}'
    webbrowser.get(inc()).open_new_tab(url)

def translate():
    txt = input("Введите текст для перевода: ")
    url = f'https://translate.google.com/?source=gtx&sl=auto&tl=ru&text={txt}&op=translate'
    webbrowser.get(inc()).open_new_tab(url)

def youtube_find():
    find = input("Что ищем?: ")
    encoded_find = quote(find)  # Кодируем строку запроса
    url = f'https://www.youtube.com/results?search_query={encoded_find}'
    webbrowser.get(inc()).open_new_tab(url)

def site_chess_com():
    url = 'https://www.chess.com/analysis?tab=analysis'
    webbrowser.get(inc()).open_new_tab(url)

def URL():
    url = input("Введите ссылку на сайт: ")
    webbrowser.get(inc()).open_new_tab(url)

def main():
    print("Выберите параметры:")
    
    # Выбор действия
    print("1. google_define\n2. google_esv\n3. translate\n4. youtube\n5. site_chess_com\n6. URL")
    site = input("Ваш выбор: ").strip()

    if site == "1":
        google_define()
    elif site == "2":
        google_esv()
    elif site == "3":
        translate()
    elif site == "4":
        youtube_find()
    elif site == "5":
        site_chess_com()
    elif site == "6":
        URL()

if __name__ == '__main__':
    main()
