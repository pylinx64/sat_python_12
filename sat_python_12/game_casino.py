# Здесь начинается игра
import random # импортирует библиотеку с командами рандома

number_random = random.randint(1, 1) # возвращает число, напр 10

number_random = str(number_random)  # число 10 превращает в число "10"

print("-> Приветсвую тебя в казино! <-")

number_player = input("-> Угадай число: ")


if number_random == number_player:
	print("-> You win 10 $$$")
else:
	print("-> Game over @@@")
