'''
try:
	name = input()
	name = int(name)
	print(name * 10)
except:
	print('Error')
'''

import colorama, tqdm, time
from colorama import Fore

for x in tqdm.tqdm(range(100), colour='Yellow', ascii=True, desc=Fore.YELLOW+'Loading...'):
	time.sleep(0.01)

colorama.init()
print(Fore.GREEN + 'Done')



name = ['A', 'l', 'e', 'x']
colors = [Fore.GREEN, Fore.YELLOW, Fore.CYAN, Fore.RED]
i = 0
while i < len(name):
	print(colors[i] + name[i], end='') 
	i += 1
	
