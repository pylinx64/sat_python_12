import time
from PIL import ImageDraw, Image, ImageFont
from datetime import datetime, timedelta

# переменные для времени и координат
FONT_SIZE = 50
TEXT_Y_POSITION = 1
TEXT_X_POSITION = 1
KIEV_UTC = 2 #укажите ваш часовой пояс 

def convert_time_to_string(dt):
	'''Обновляет время по Киеву'''
    dt += timedelta(hours=KIEV_UTC)
    return f"{dt.hour}:{dt.minute:02}"
