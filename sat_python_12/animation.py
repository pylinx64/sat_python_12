import pygame

# инициализируем движок
pygame.init()

# цвета
black = (   0,   0,   0)
white = ( 255, 255, 255)
green = (   0, 255,   0)
red   = ( 255,   0,   0)
blue  = (   0,   0, 255)

# Загружает картинку png
dvd_surf = pygame.image.load('dvd.png')

# задает ширину и высоту экрана
size = [1280, 961]
screen = pygame.display.set_mode(size)

# установка заголовка окна
pygame.display.set_caption("Cool ITFriends Game")


# Останавливается в цикле, пока игрок не нажмет на кнопку закрыть
done = False

# Используется для FPS
clock = pygame.time.Clock()

# Начальная позиция прямоугольника
rect_x = 50
rect_y = 50

# Скорость прямоугольника
rect_speed_x = 5
rect_speed_y = 5


#-------------------Основной цикл программы-------------------
while done == False:
	# ОБРАБОТКА ВСЕХ СОБЫТИЙ 
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	# ОБРАБОТКА ВСЕХ СОБЫТИЙ 
	
	
	# ЛОГИКА ИГРЫ
	
	# ЛОГИКА ИГРЫ
	
	
	# ВЕСЬ КОД РИСОВАНИЯ
	# Очистить экран и установить белый фон
	screen.fill(black) 
	
	# Прямоугольник
	rect_surf = pygame.draw.rect(screen, white, [rect_x, rect_y, 50, 50])
	#pygame.draw.rect(screen, red, [rect_x+10, rect_y+10, 30, 30])
	
	# Двигаем прямоугольник
	rect_x += rect_speed_x
	rect_y += rect_speed_y
	
	# Проверка на границы экрана
	if rect_y > 911 or rect_y < 0:
		rect_speed_y = rect_speed_y * -1
	if rect_x > 1230 or rect_x < 0:
		rect_speed_x = rect_speed_x * -1

	# отрисовуем картинку
	screen.blit(dvd_surf, rect_surf)
	
	# ВЕСЬ КОД РИСОВАНИЯ
	
	# Обновить экран, чтобы увидеть рисунок
	pygame.display.flip()
	
	# Ограничить до 60 кадров
	clock.tick(60)

# Правильное выключение игры 
pygame.quit()

