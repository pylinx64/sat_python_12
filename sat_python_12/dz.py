print('alex')				# функция
number = 12					# переменная
print(number)

import random				# импорт библиотеки
r = random.randint(1, 5)	# используем библиотеку

							# условия/проверка
if r == 1:					# если
	print('Ok')
elif r == 2:				# тоже если
	print('ne Ok')
else:						# иначе
	print('mmm...')

l_number = [0, 1, 2, 3, 4]	# список
for i in l_number:			# цикл for in
	print(i)				
		
i = 0						# счетчик 
while i < 5:				# цикл while
	print(i)
	i = i + 1				# обновляем счетчик (+1)
