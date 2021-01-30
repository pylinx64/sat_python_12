import random
import time

list_win = ["car", "house", "ps5", "кабачек", "minecraft"]

print("> Выйграй приз <")
print(list_win)

money = input('Введите кэш: ')
money = int(money)

if money > 24:
	print("Игра началась...")
	print(3)
	print(2)
	print(1)
	random_win = random.choice(list_win)
	print("Вы выиграли - ", random_win)
else:
	print("Деньги закончились ((")

print("Денег - ", money)
