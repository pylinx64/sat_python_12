import pygame

# инициализируем движок
pygame.init()

# цвета
black = (   0,   0,   0)
white = ( 255, 255, 255)
green = (   0, 255,   0)
red   = ( 255,   0,   0)

# задает ширину и высоту экрана
size = [1280, 961]
screen = pygame.display.set_mode(size)

# установка заголовка окна
pygame.display.set_caption("Cool ITFriends Game")


# Останавливается в цикле, пока игрок не нажмет на кнопку закрыть
done = False

# Используется для FPS
clock = pygame.time.Clock()

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
	
	# Залить задний фон
	screen.fill(white)
	
	# Рисует прямую линию
	pygame.draw.line(screen, red, [1, 2], [500, 500], 15)
	
	# ВЕСЬ КОД РИСОВАНИЯ
	
	# Обновляет экран
	pygame.display.flip()
	
	# Ограничить до 60 кадров
	clock.tick(60)

# Правильное выключение программы на pygame
pygame.quit()

