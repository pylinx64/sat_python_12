from telethon import TelegramClient, sync
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
from datetime import datetime
import time
from config import *
from time_generate import *

# Подключение к серверу tg
client = TelegramClient('ananas', api_id, api_hash)
client.start()

# 
while True:
	# TODO: функция для создания фоток
    change_img()
    # удаляет все фотки с акк tg 
    client(DeletePhotosRequest(client.get_profile_photos('me')))
    # файл сохраняет в переменной
    file = client.upload_file(f"time.png")
    # обновляет фото профиля
    client(UploadProfilePhotoRequest(file))
    # задержка
    time.sleep(60)
