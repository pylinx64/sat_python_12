import random
game = []

while True:
	if random.randint(0, 1) == 0: 
		game.append('bandit')
	if random.randint(0, 1) == 1: 	
		game.append('player')
	if len(game) > 52:
		break

print(game)


