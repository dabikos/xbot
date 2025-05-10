import requests
from bs4 import BeautifulSoup
from telegram import Bot
import time

# Настройки
TWITTER_USERNAME = "macallanft"
CHECK_INTERVAL = 300  # Проверка каждые 5 минут
TELEGRAM_TOKEN = "7892885574:AAEGIl4IGOTyATTGA6_JRMl-OKa2xd68MBk"
CHAT_ID = 706156303

# Инициализация Telegram-бота
bot = Bot(token=TELEGRAM_TOKEN)

# Предыдущие значения
last_name = None
last_avatar = None

def get_twitter_profile(username):
    url = f"https://twitter.com/{username}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    # Имя
    name_tag = soup.find("meta", {"property": "og:title"})
    name = name_tag["content"] if name_tag else None

    # Аватарка
    img_tag = soup.find("img", {"alt": "Image"})
    avatar = img_tag["src"] if img_tag else None

    return name, avatar

def send_telegram_message(message):
    bot.send_message(chat_id=CHAT_ID, text=message)

while True:
    try:
        name, avatar = get_twitter_profile(TWITTER_USERNAME)
        changed = False
        msg = f"Изменения у @{TWITTER_USERNAME}:\n"

        if last_name and name != last_name:
            msg += f"Имя: {last_name} → {name}\n"
            changed = True

        if last_avatar and avatar != last_avatar:
            msg += f"Аватар изменён.\nСтарый: {last_avatar}\nНовый: {avatar}\n"
            changed = True

        if changed:
            send_telegram_message(msg)

        last_name = name
        last_avatar = avatar

    except Exception as e:
        print("Ошибка:", e)

    time.sleep(CHECK_INTERVAL_
